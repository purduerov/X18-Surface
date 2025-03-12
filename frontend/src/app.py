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

class Frontend(Node):
    def __init__(self):
        super().__init__("frontend")
        self.get_logger().info("Frontend node started")

        # Setup the heartbeat helper
        self.heartbeat_helper = HeartbeatHelper(self)
    
        # Setup the flask app
        self.app = Flask(__name__)
        CORS(self.app)
        self.socketio = SocketIO(self.app)
        load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")

        # Setup the routes
        self.setup_routes()

        # Setup the socketio events
        self.setup_socketio_events()

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
        # 4 Camera streams
        @self.app.route("/")
        def index():
            return render_template("index.html")

        # Node status page
        @self.app.route("/node-status")
        def node_status():
            return render_template("node_status.html")

        @self.app.route("/big-stream")
        def big_stream():
            return render_template("index.html", rov_ip=os.getenv("ROV_IP"))
        
        # The new UI
        @self.app.route("/ui")
        def new_ui():
            return render_template("innovative_ui.html", rov_ip=os.getenv("ROV_IP"))
        
        # The demo subscriber page
        @self.app.route("/demo-subscriber")
        def demo_subscriber():
            return render_template("demo_ros_subscriber.html")
        
        # The thrust testing page
        @self.app.route("/thruster-testing")
        def thrust_testing():
            return render_template("thruster_testing.html")
        
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
            # Ignore heartbeat events
            if event == "heartbeat":
                return
            if event.startswith("frontend-"):
                # self.get_logger().info(f"Handling frontend event: {event}, data: {data}")
                # Handle the event
                handle_frontend_event(self, event, data)
            else:
                # self.get_logger().info(f"Emitting to frontend: {event}, data: {data}")
                # Forward the event and its data back to the client
                self.socketio.emit(event, data)


def main():
    rclpy.init()
    frontend = Frontend()
    rclpy.spin(frontend)

if __name__ == "__main__":
    main()
