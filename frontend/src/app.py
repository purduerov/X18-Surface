#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, url_for
from ssh import Ssh
from streams import Streams
from signal_handler import SignalHandler
import rclpy
import signal
from flask_socketio import SocketIO
from dotenv import load_dotenv
import threading
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")


@app.route("/")
def index():
    return render_template("index.html", rov_ip=os.getenv("ROV_IP"))


@app.route("/demo_ros_subscriber")
def demo_ros_subscriber():
    return render_template("demo_ros_subscriber.html")


@socketio.on('connect')
def handle_connect():
    node.get_logger().info('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    node.get_logger().info('Client disconnected')

@socketio.on('count')
def handle_count(data):
    node.get_logger().info(f"Received count: {data}")
    # Forward the data to the client
    socketio.emit('count', data)



def initialize_frontend_nodes():
    """
    Initializes the ROS node for the Flask server
    Returns the node object
    """
    rclpy.init()
    node = rclpy.create_node("flask_server")
    node.get_logger().info("Flask server started")
    return node


def establish_rov_connection(node):
    """
    Establishes a connection to the ROV
    Return the SSH client object
    """
    ssh = Ssh(node)
    rov_connection = ssh.connect()
    return rov_connection


def establish_camera_streams(node, rov_connection):
    """
    Starts the camera streams on the ROV
    Returns a boolean indicating if the camera streams started successfully
    """
    camera_streams = Streams(node, rov_connection)
    camera_streams.run_camera_streams()
    return camera_streams

def ros_spin(node):
    """
    Spins the Demo Subscriber ROS node
    """
    rclpy.spin(node)


if __name__ == "__main__":
    """
    Main function for running the ROV
    To build the program, run `scripts/build.sh`
    To run the program, run `scripts/run.sh`
    """
    node = initialize_frontend_nodes()
    if node is None:
        print("ERROR: Could not initialize ROS node")
        exit(1)

    # Subscribe to ROS topics using subscriber.py

    # rov_connection = establish_rov_connection(node)
    # if rov_connection is None:
    #     exit(1)

    # camera_streams = establish_camera_streams(node, rov_connection)
    # if camera_streams is False:
    #     exit(1)

    # Establish the signal handler for closing the application
    # signal_handler = SignalHandler(node, rov_connection, camera_streams)
    # signal.signal(signal.SIGINT, signal_handler.close_application)

    # app.run(host="0.0.0.0", port=5000)

    # Run the Flask app with SocketIO
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)
