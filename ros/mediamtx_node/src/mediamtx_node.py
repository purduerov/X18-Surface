#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from utils.heartbeat_helper import HeartbeatHelper
import socket
import os
import subprocess
import threading

# Create a publisher node that will publish a message counting up and down from 100 repeatedly
class MediaMTXNode(Node):
    def __init__(self):
        super().__init__('mediamtx_node')

        self.heartbeat_helper = HeartbeatHelper(self)
    
        # Create publisher to publish ip address to the topic /surface_ip
        self.publisher = self.create_publisher(String, 'surface_ip', 10)
        self.timer = self.create_timer(1.0, self.publish_ip_address)
        self.ip_pub_count = 0
        self.ip_pub_count_max = 10

        # Create a subscriber to listen to the topic /surface_ip
        self.create_subscription(String, 'surface_ip', self.ip_callback, 10)

        # Start the MediaMTX server process and monitor the process and watch for certain events and messages
        self.start_mediamtx_server()

    def publish_ip_address(self):
        msg = String()
        # Get the ip address of the surface computer
        ip = self.get_local_ip()
        self.get_logger().info(f"Publishing IP address: {ip}")
        msg.data = ip
        self.publisher.publish(msg)
        self.ip_pub_count += 1
        if self.ip_pub_count >= self.ip_pub_count_max:
            self.get_logger().info("Stopping publishing IP address")
            self.timer.cancel()

    def get_local_ip(self):
        try:
            # Create a socket and connect to a public server
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))  # Google's public DNS server
                local_ip = s.getsockname()[0]
            return local_ip
        except Exception as e:
            return f"Error getting local IP: {e}"
        
    def ip_callback(self, msg):
        # Check if "STOP" was received, if so stop publishing the ip address
        if msg.data == "STOP":
            self.timer.cancel()
            self.get_logger().info("Stopped publishing IP address")

    def start_mediamtx_server(self):
        def start_server():
            # Start the MediaMTX server process
            self.get_logger().info("Starting MediaMTX server")
            # Ensure the executable is present before executing
            if os.path.exists("install/mediamtx_node/lib/mediamtx_node/mediamtx"):
                self.get_logger().info("MediaMTX server executable found")
            else:
                self.get_logger().error("MediaMTX server executable not found")
                return
            
            # Start the MediaMTX server process
            self.get_logger().info("Starting MediaMTX server process")
            self.process = subprocess.Popen(["install/mediamtx_node/lib/mediamtx_node/mediamtx", "install/mediamtx_node/lib/mediamtx_node/mediamtx.yml"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            while True:
                for line in self.process.stdout:
                    self.get_logger().info(line.strip())
                for line in self.process.stderr:
                    self.get_logger().error(line.strip())
                if self.process.poll() is not None:
                    self.get_logger().info("MediaMTX server process has terminated")
                    break

        # Start the server in a separate thread
        server_thread = threading.Thread(target=start_server)
        server_thread.start()


def main():
    rclpy.init()
    publisher_node = MediaMTXNode()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
