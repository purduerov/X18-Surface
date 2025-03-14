#!/usr/bin/env python3

# Standard imports
import os
import sys
import signal
import threading

# External imports
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from flask_cors import CORS
from dotenv import load_dotenv
import rclpy
from rclpy.node import Node

# Local imports
from utils.heartbeat_helper import HeartbeatHelper
from frontend.src.frontend_utils.frontend_handler import handle_frontend_event
from frontend.src.frontend_utils.log_helper import LogHelper
from frontend.src.frontend_utils.recording_api import RecordingRoutes  # Import the new module

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

        # Setup the log helper
        self.log_helper = LogHelper(self.socketio, self.get_logger())

        ### ----- ROUTE SETUP ----- ###
        self.setup_routes()
        self.recording_routes = RecordingRoutes(self.app, self.get_logger())

        ### ----- SOCKETIO SETUP ----- ###
        self.setup_socketio_events()
        self.log_helper.setup_socket_events()
    
        ### ----- START SERVICES ----- ###
        # Start flask
        self.flask_thread = threading.Thread(target=self.run_flask)
        self.flask_thread.start()
        self.log_helper.start_log_monitor()  # Log helper

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
        
        ### -------- UTILITY PAGES -------- ###

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
        def recordings_page():
            return render_template("recordings.html", active_page='recordings')
                
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
                # self.get_logger().info(f"Ignoring event: {event}, data: {data}")
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
        os._exit(0)  # exit immediately without cleanup
    
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
