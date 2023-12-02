#!/usr/bin/env python3

# TODO: Refine error handling across all files

import sys
import rclpy
import threading
from PyQt5.QtWidgets import QApplication
from main import MainWindow
from ThrustersSurface import ThrustersSurfaceNode
from DepthSurface import DepthSurfaceNode
import multiprocessing

from interface import Ui_MainWindow
from ssh import ssh
from streams import streams
from gamepad import gamepad


def run_ros_node(node):
 # node = node(window=window)
 rclpy.spin(node)
 rclpy.shutdown()


def run_multiple_nodes(nodes):
 while True:
        for node in nodes:
            rclpy.spin_once(node, timeout_sec=0.1)


def main():
    rclpy.init()

    print("Starting SSH processes...")
    ssh = ssh()
    connection = ssh.connect()

    print("Starting camera stream processes...")
    streams = streams(connection)
    streams.start()

    # print("Connecting gamepad...")
    # TODO: this

    app = QApplication(sys.argv)
    window = MainWindow()

    print("Connecting fronted ros nodes...")
    thrusters = ThrustersSurfaceNode(window=window)
    depth = DepthSurfaceNode(window=window)
    nodelist = [thrusters, depth]
    node_thread = threading.Thread(target=run_multiple_nodes, args=(nodelist,))
    node_thread.daemon = True
    node_thread.start()

    print("Starting application...")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
