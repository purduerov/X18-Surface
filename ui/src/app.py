#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, url_for
from ssh import Ssh
from streams import Streams
import rclpy
import signal


app = Flask(__name__)
global global_node, global_rov_connection, global_streams, global_shutdown
global_node = None
global_rov_connection = None
global_streams = None
global_shutdown = False


def close_app(signal, frame):
    """
    Closing the application
    Triggered when the user presses Ctrl+C
    Camera streams are closed and the SSH connection is closed
    """

    global global_node, global_rov_connection, global_streams, global_shutdown
    
    if global_shutdown:
        return
    global_shutdown = True
    
    try:
        if global_node is not None:
            global_node.get_logger().info("Closing application")  
        
        if global_streams is not None:
            global_streams.close_camera_streams()
            if global_node is not None:
                global_node.get_logger().info("Camera streams closed")

        if global_rov_connection is not None:
            global_rov_connection.close()
            if global_node is not None:
                global_node.get_logger().info("Connection to ROV closed")
        
        if global_node is not None:
            global_node.destroy_node()

        rclpy.shutdown()
        
    except Exception as e:
        if global_node is not None:
            global_node.get_logger().error("Error during shutdown: " + str(e))
    
    print("Application closed")
    exit(0)


signal.signal(signal.SIGINT, close_app)


@app.route('/')
def index():
    return render_template('index.html')


def initialize_frontend_nodes():
    """
    Initializes the ROS node for the Flask server
    Returns the node object
    """
    rclpy.init()
    node = rclpy.create_node('flask_server')
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
    """
    streams = Streams(node, rov_connection)
    streams.run_camera_streams() 
    return streams


if __name__ == '__main__':
    """ 
    Main function for running the ROV
    To build the program, run `scripts/build.sh`
    To run the program, run `scripts/run.sh`
    """
    node = initialize_frontend_nodes()
    if node is None:
        print("ERROR: Could not initialize ROS node")
        exit(1)
    else:
        global_node = node

    rov_connection = establish_rov_connection(node)
    if rov_connection is None:
        node.get_logger().error("ERROR: Could not establish connection to ROV")
        exit(1)
    else:
        global_rov_connection = rov_connection

    streams = establish_camera_streams(node, rov_connection)
    if streams is None:
        node.get_logger().error("ERROR: Could not start camera streams")
        exit(1)
    else:
        global_streams = streams

    app.run(host='0.0.0.0', port=5000)