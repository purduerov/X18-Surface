#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
import socketio
import json
import os
from dotenv import load_dotenv

sio = socketio.Client()

class HeartbeatMonitor(Node):
    def __init__(self):
        super().__init__('heartbeat_monitor')
        self.create_subscription(Header, 'heartbeat', self.heartbeat_callback, 10)
        self.heartbeat_status = {}  # Tracks the last timestamp for each node
        self.timer = self.create_timer(2.0, self.emit_heartbeats)  # Check every 2 seconds

        # Expected node names dictionary (node name: last seen timestamp)
        self.expected_surface_nodes = {"frontend": 0, "controller": 0, "mediamtx_node": 0, "ui_subscriber": 0}
        self.expected_core_nodes = {"ROV_main": 0, "thrust_control": 0, "thrust_to_spi": 0}

    def heartbeat_callback(self, msg):
        node_name = msg.frame_id  # The node's unique identifier
        timestamp = self.get_clock().now().nanoseconds  # Current time
        self.heartbeat_status[node_name] = timestamp  # Update last seen time
        if node_name in self.expected_surface_nodes:
            self.expected_surface_nodes[node_name] = timestamp  # Update last seen time for surface nodes
        # Uncomment and modify the following line if you have core nodes
        if node_name in self.expected_core_nodes:
            self.expected_core_nodes[node_name] = timestamp  # Update last seen time for core nodes
        # Emit the heartbeat to the frontend using SocketIO

        # self.get_logger().info(f'Heartbeat received from {node_name}')


    def emit_heartbeats(self):
        current_time = self.get_clock().now().nanoseconds
        timeout = 5 * 1e9  # 5 seconds in nanoseconds
        # Emit the heartbeat status for each surface node
        for node_name, last_seen in self.expected_surface_nodes.items():
            if current_time - last_seen > timeout:
                self.get_logger().warn(f'No heartbeat from {node_name}')
                sio.emit('heartbeat', json.dumps({'node': node_name, 'status': 'inactive', 'location': 'surface'}))
            else:
                sio.emit('heartbeat', json.dumps({'node': node_name, 'status': 'active', 'location': 'surface'}))
        # Emit the heartbeat status for each core node
        for node_name, last_seen in self.expected_core_nodes.items():
            if current_time - last_seen > timeout:
                self.get_logger().warn(f'No heartbeat from {node_name}')
                sio.emit('heartbeat', json.dumps({'node': node_name, 'status': 'inactive', 'location': 'core'}))
            else:
                sio.emit('heartbeat', json.dumps({'node': node_name, 'status': 'active', 'location': 'core'}))
                

def main(args=None):
    rclpy.init(args=args)
    monitor = HeartbeatMonitor()

    # Connect to the SocketIO server
    load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")
    port = str(os.getenv("FLASK_PORT", 5013))
    sio.connect('http://127.0.0.1:' + port)  # Adjust the URL if necessary
    
    rclpy.spin(monitor)
    monitor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()