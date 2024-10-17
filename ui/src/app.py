#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, url_for
from ssh import Ssh
from streams import Streams
from signal_handler import SignalHandler
import rclpy
import signal


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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

    rov_connection = establish_rov_connection(node)
    if rov_connection is None:
        exit(1)

    camera_streams = establish_camera_streams(node, rov_connection)
    if camera_streams is False:
        exit(1)

    # Establish the signal handler for closing the application
    signal_handler = SignalHandler(node, rov_connection, camera_streams)
    signal.signal(signal.SIGINT, signal_handler.close_application)

    app.run(host="0.0.0.0", port=5000)
