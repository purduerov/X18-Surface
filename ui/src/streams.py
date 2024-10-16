import paramiko
import time


class Streams:

    def __init__(self, node, rov_connection):
        self.node = node
        self.rov_connection = rov_connection
    

    def run_camera_streams(self):
        self.node.get_logger().info("Starting camera streams...")
        self.rov_connection.exec_command("cd cameras2 && ./mediamtx")
        # run confirmation
        # logging the output will not work
        # logging the running processes (somehow) terminates the mediamtx process
        self.node.get_logger().info("Camera streams started")
        self.node.get_logger().warning("Camera streams can take a few minutes to start")


    def close_camera_streams(self):
        self.node.get_logger().info("Closing camera streams...")
        self.rov_connection.exec_command("killall mediamtx")
        # run confirmation
        self.node.get_logger().info("Camera streams closed")