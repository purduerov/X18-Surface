#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, url_for
# Import rlcpy for logging
import rclpy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # Initialize the ros node
    rclpy.init()
    node = rclpy.create_node('flask_server')
    node.get_logger().info("Flask server started")

    # Run the flask app
    app.run(host='0.0.0.0', port=5000)