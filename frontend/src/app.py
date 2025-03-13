#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import rclpy
from rclpy.node import Node
import signal
from flask_socketio import SocketIO
from dotenv import load_dotenv
import threading
from flask_cors import CORS
from utils.heartbeat_helper import HeartbeatHelper
from frontend_handler import handle_frontend_event
import sys
from log_helper import LogHelper
import requests
import json
from datetime import datetime
import glob
import uuid
import subprocess
from flask import send_file, abort, session
import re

MEDIAMTX_API = "http://localhost:9997/v3"

class Frontend(Node):
    def __init__(self):
        super().__init__("frontend")
        self.get_logger().info("Frontend node started")

        # Setup the heartbeat helper
        self.heartbeat_helper = HeartbeatHelper(self)

        # Setup the flask app
        self.app = Flask(__name__)
        CORS(self.app)
        # Add a secret key for the session
        self.socketio = SocketIO(self.app)
        load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")
        
        # Store the project root directory
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        self.get_logger().info(f"Project root directory: {self.project_root}")

        # Setup the log helper
        self.log_helper = LogHelper(self.socketio, self.get_logger())

        # Setup the routes
        self.setup_routes()

        # Setup the socketio events
        self.setup_socketio_events()

        # Setup log-related socket events
        self.log_helper.setup_socket_events()
        
        # Start log monitoring
        self.log_helper.start_log_monitor()

        # Run the Flask app with SocketIO
        self.flask_thread = threading.Thread(target=self.run_flask)
        self.flask_thread.start()

        # Setup publishers
        self.final_thrust_pub = None

    def run_flask(self):
        port = int(os.getenv("FLASK_PORT", 5013))
        self.socketio.run(
            self.app, host="0.0.0.0", port=port, allow_unsafe_werkzeug=True
        )

    # Function to setup the routes for the Flask app
    def setup_routes(self):
        # Default Route
        @self.app.route("/")
        def index():
            return redirect(url_for("new_ui"), code=302)
        
        # Main UI
        @self.app.route("/ui")
        def new_ui():
            return render_template("innovative_ui.html")
        
        ### -------- CAMERA PAGES -------- ###

        @self.app.route("/all-cameras")
        def all_cameras():
            return render_template("all_cameras.html", active_page='all-cameras')
        
        @self.app.route("/fullscreen-camera")
        def fullscreen_camera():
            camera = request.args.get('camera', '1')  # Default to camera 1 if not specified
            return render_template("fullscreen_camera.html", active_page='fullscreen-camera', camera=camera)
        
        ### -------- DEBUG PAGES -------- ###

        # The thrust testing page
        @self.app.route("/thruster-testing")
        def thrust_testing():
            return render_template("thruster_testing.html", active_page='thruster-testing')
        
        # Node status page
        @self.app.route("/node-status")
        def node_status():
            return render_template("node_status.html", active_page='node-status')
        
        # Logs page
        @self.app.route("/logs")
        def logs():
            return render_template("logs.html", active_page='logs')
        
        # Recordings page
        @self.app.route("/recordings")
        def recordings():
            return render_template("recordings.html", active_page='recordings')
        
        # Add these imports and routes to your Flask application
        @self.app.route('/api/record/start/<camera_number>', methods=['POST'])
        def start_recording(camera_number):
            try:
                # Validate camera number
                if camera_number not in ['1', '2', '3', '4']:
                    return jsonify({'success': False, 'message': 'Invalid camera number'})
                    
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                videos_dir = os.path.join(os.getcwd(), "videos")
                output_path = os.path.join(videos_dir, f"camera_{camera_number}_{timestamp}.mp4")
                stream_url = f"rtsp://localhost:8554/camera_{camera_number}"

                # Ensure the videos directory exists
                os.makedirs(videos_dir, exist_ok=True)
                
                # Use ffmpeg to start recording the stream
                command = f"ffmpeg -i {stream_url} -c copy {output_path}"
                os.system(f"nohup {command} &")
                
                return jsonify({'success': True})
                
            except Exception as e:
                return jsonify({'success': False, 'message': str(e)})

        @self.app.route('/api/record/stop/<camera_number>', methods=['POST'])
        def stop_recording(camera_number):
            try:
                # Validate camera number
                if camera_number not in ['1', '2', '3', '4']:
                    return jsonify({'success': False, 'message': 'Invalid camera number'})
                
                # Find the ffmpeg process and kill it
                stream_url = f"rtsp://localhost:8554/camera_{camera_number}"
                command = f"pkill -f 'ffmpeg -i {stream_url}'"
                os.system(command)
                
                return jsonify({'success': True})
            
            except Exception as e:
                return jsonify({'success': False, 'message': str(e)})

        @self.app.route('/api/recordings')
        def get_recordings():
            # Log current working directory
            # self.get_logger().info(f"Current working directory: {os.getcwd()}")

            # Get all MP4 files in the videos directory using absolute path
            videos_dir = os.path.join(os.getcwd(), "videos")
            mp4_files = glob.glob(os.path.join(videos_dir, "*.mp4"))

            # self.get_logger().info(f"Found {len(mp4_files)} recordings")
            
            # Create a list of recording objects with metadata
            recordings = []
            for file in mp4_files:
                # Parse the filename to get camera and timestamp
                filename = os.path.basename(file)
                
                # Get file creation time
                creation_time = os.path.getctime(file)
                
                # Get video duration using ffprobe
                duration = "00:00"
                try:
                    result = subprocess.run(
                    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                    )
                    
                    if result.stdout:
                        # Convert seconds to MM:SS format
                        seconds = float(result.stdout)
                        minutes = int(seconds // 60)
                        seconds = int(seconds % 60)
                        duration = f"{minutes:02d}:{seconds:02d}"
                except Exception as e:
                    self.get_logger().error(f"Error getting video duration: {str(e)}")
                
                # Extract date from filename
                date_match = re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', filename)
                date = date_match.group(1) if date_match else datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d_%H-%M-%S")
                
                recordings.append({
                    'id': filename,  # Use filename directly as ID
                    'filename': filename,
                    'date': date,
                    'creation_time': creation_time,
                    'size': os.path.getsize(file),
                    'duration': duration
                })

            # Sort by creation time, newest first
            recordings.sort(key=lambda x: x['creation_time'], reverse=True)
            
            return jsonify(recordings)

        @self.app.route('/api/recordings/<path:filename>/thumbnail')
        def get_recording_thumbnail(filename):
            self.get_logger().info(f"Getting thumbnail for recording: {filename}")
            # Use absolute path for the video file
            file_path = os.path.join(os.getcwd(), 'videos', filename)
            self.get_logger().info(f"Path: {file_path}")
            if not os.path.exists(file_path):
                self.get_logger().error(f"Recording not found: {filename}")
                abort(404)
            
            thumbnail_dir = os.path.join(os.getcwd(), 'videos', 'thumbnails')
            os.makedirs(thumbnail_dir, exist_ok=True)
            thumbnail_path = os.path.join(thumbnail_dir, f"{hash(filename)}.jpg")
            
            if not os.path.exists(thumbnail_path):
                try:
                    subprocess.run([
                        'ffmpeg', '-y', '-i', file_path, '-ss', '00:00:01.000', 
                        '-vframes', '1', thumbnail_path
                    ], check=True)
                except Exception as e:
                    self.get_logger().error(f"Error generating thumbnail: {str(e)}")
                    return send_file('static/default-thumbnail.jpg', mimetype='image/jpeg')
            
            return send_file(thumbnail_path, mimetype='image/jpeg')

        @self.app.route('/api/recordings/<path:filename>/play')
        def play_recording(filename):
            # Construct the absolute path
            filename = os.path.join(os.getcwd(), 'videos', filename)

            if not os.path.exists(filename):
                self.get_logger().error(f"Recording not found: {filename}")
                abort(404)
            
            return send_file(filename, mimetype='video/mp4')

        @self.app.route('/api/recordings/<path:filename>/download')
        def download_recording(filename):
            # Construct the absolute path
            filename = os.path.join(os.getcwd(), 'videos', filename)
            
            if not os.path.exists(filename):
                self.get_logger().error(f"Recording not found: {filename}")
                abort(404)
            
            video_path = os.path.abspath(filename)
            return send_file(video_path, mimetype='video/mp4', as_attachment=True)

        @self.app.route('/api/recordings/<path:filename>', methods=['DELETE'])
        def delete_recording(filename):
            # Construct the absolute path
            filename = os.path.join(os.getcwd(), 'videos', filename)
            if not os.path.exists(filename):
                return jsonify({'success': False, 'message': 'Recording not found'})
            
            try:
                # Delete the recording file
                os.remove(filename)
                
                # Delete the thumbnail if it exists
                thumbnail_path = os.path.join(os.getcwd(), 'thumbnails', f"{hash(filename)}.jpg")
                if os.path.exists(thumbnail_path):
                    os.remove(thumbnail_path)
                
                return jsonify({'success': True})
            except Exception as e:
                return jsonify({'success': False, 'message': str(e)})
                        
    # Function to setup the socketio events
    def setup_socketio_events(self):
        @self.socketio.on("connect")
        def connect():
            self.get_logger().info("SocketIO connected")

        @self.socketio.on("disconnect")
        def disconnect():
            self.get_logger().info("SocketIO disconnected")

        # General-purpose event handler
        @self.socketio.on("*")  # Using '*' to catch all events
        def handle_all_events(event, data=None):
            # Handle frontend events
            if event.startswith("frontend-"):
                # self.get_logger().info(f"Handling frontend event: {event}, data: {data}")
                # Handle the event
                handle_frontend_event(self, event, data)
            
            # Ignore heartbeat events
            elif event.startswith("request_logs") or event.startswith("clear_logs"):
                # self.get_logger().info(f"Unhandled event: {event}, data: {data}")
                return

            # Forward all other events
            else:
                # self.get_logger().info(f"Unhandled event: {event}, data: {data}")
                self.socketio.emit(event, data)

def main():
    rclpy.init()
    frontend = Frontend()
    
    # Silent exit on SIGINT - just terminate immediately
    def silent_exit(sig, frame):
        # Exit without any logging or cleanup
        frontend.log_helper.stop_log_monitor()
        os._exit(0)  # Use os._exit() to exit immediately without cleanup
    
    # Register the signal handler
    signal.signal(signal.SIGINT, silent_exit)
    signal.signal(signal.SIGTERM, silent_exit)
    
    try:
        rclpy.spin(frontend)
    except KeyboardInterrupt:
        # Exit silently on KeyboardInterrupt too
        os._exit(0)
    finally:
        # This will only run if spin() returns normally, not after os._exit()
        frontend.log_helper.stop_log_monitor()
        sys.exit(0)

if __name__ == "__main__":
    main()
