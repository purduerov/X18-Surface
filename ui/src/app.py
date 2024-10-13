#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, url_for
from ssh import Ssh

# Import rlcpy for logging
import rclpy

app = Flask(__name__)


@app.route("/")
def index():

    # TODO: Add the four camera streams to the index.html file

    return render_template("index.html")


def initialize_ros_nodes():
    # Initialize the ros node
    rclpy.init()
    node = rclpy.create_node("flask_server")
    node.get_logger().info("Flask server started")

    return node


def connect(node):
    ssh = Ssh()
    ssh.connect(node)
    ssh.close()


if __name__ == "__main__":

    # Initialize the ROS nodes
    node = initialize_ros_nodes()
    if node is None:
        print("ERROR: Could not initialize ROS node")
        exit(1)

    # Connect to the ROV
    connect(node)

    # Run the flask app
    app.run(host="0.0.0.0", port=5000)
