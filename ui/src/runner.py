#!/usr/bin/env python3

# TODO: Refine error handling across all files

import sys
import rclpy
import threading
from PyQt5.QtWidgets import QApplication
from main import MainWindow
from ThrustersSurface import ThrustersSurfaceNode
from DepthSurface import DepthSurfaceNode
from GamepadListener import GamepadSurfaceNode
import multiprocessing

from interface import Ui_MainWindow
from ssh import ssh
from streams import streams
from gamepad import gamepad
from GamepadSender import GamepadNode


def run_multiple_nodes(nodes):
    while True:
        for node in nodes:
            rclpy.spin_once(node, timeout_sec=0.01)


def main():
    rclpy.init()

    print("Starting SSH processes...")
    ssh_comm = ssh()
    connection = ssh_comm.connect()
    try:
        print("Starting camera stream processes...")
        streams_comm = streams(connection)
        streams_comm.start()

        #print("Connecting gamepad...")
        # TODO: this
        gamepad = GamepadNode()

        app = QApplication(sys.argv)
        window = MainWindow(ssh_comm)

        print("Connecting fronted ros nodes...")
        thrusters = ThrustersSurfaceNode(window=window)
        depth = DepthSurfaceNode(window=window)
        surfacegp = GamepadSurfaceNode(window=window)
        nodelist = [thrusters, depth, surfacegp, gamepad]
        node_thread = threading.Thread(
            target=run_multiple_nodes, args=(nodelist,))
        node_thread.daemon = True
        node_thread.start()

        print("Starting application...")
        window.show()
        while(app.exec_()):
            pass
        streams_comm.stop()
        sys.exit(1)
    except Exception as e:
        ssh_comm.close()
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
