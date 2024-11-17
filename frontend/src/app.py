#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, url_for
from ssh import Ssh
from streams import Streams
from signal_handler import SignalHandler
import rclpy
from rclpy.node import Node
import signal
from flask_socketio import SocketIO
from dotenv import load_dotenv
import threading
from flask_cors import CORS


class Frontend(Node):
    def __init__(self):
        super().__init__("frontend")
        self.get_logger().info("Frontend node started")

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
        self.socketio.run(self.app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)

    # Function to setup the routes for the Flask app
    def setup_routes(self):
        # 4 Camera streams
        @self.app.route("/")
        def index():
            return render_template("index.html", rov_ip=os.getenv("ROV_IP"))
        
        # The new UI
        @self.app.route("/new-ui")
        def new_ui():
            return render_template("new_index_proto.html")
        
        # The demo subscriber page
        @self.app.route("/demo-subscriber")
        def demo_subscriber():
            return render_template("demo_ros_subscriber.html")
        
    # Function to setup the socketio events
    def setup_socketio_events(self):
        @self.socketio.on("connect")
        def connect():
            self.get_logger().info("SocketIO connected")
        
        @self.socketio.on("disconnect")
        def disconnect():
            self.get_logger().info("SocketIO disconnected")

        @self.socketio.on('count')
        def handle_count(data):
            # self.get_logger().info(f"Flask received count: {data}")
            # Forward the data to the client
            self.socketio.emit('count', data)

        @self.socketio.on('rov_velocity')
        def handle_rov_velocity(data):
            # self.get_logger().info(f"Flask received rov_velocity: {data}")
            # Parse the data and forward it to the client
            self.socketio.emit('rov_velocity', data)
        
        @self.socketio.on('surface_imu')
        def handle_surface_imu(data):
            self.socketio.emit('surface_imu', data)


def main():
    rclpy.init()
    frontend = Frontend()
    rclpy.spin(frontend)
    frontend.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()