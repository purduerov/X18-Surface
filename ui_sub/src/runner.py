#!/usr/bin/env python3

import sys
import rclpy
import threading
from PyQt5.QtWidgets import QApplication
from GUI import MainWindow
from ThrustersSurface import ThrustersSurfaceNode
from DepthSurface import DepthSurfaceNode
def run_ros_node(window, node):
    node = node(window=window)
    rclpy.spin(node)
    rclpy.shutdown()

def run_multiple_nodes(nodes):
    while True:
        for node in nodes:
            rclpy.spin_once(node)


def main():

    rclpy.init()
    app = QApplication(sys.argv) 
    window = MainWindow()
    
    '''
    thruster_thread = threading.Thread(target=run_ros_node, args=(window,ThrustersSurfaceNode))
    thruster_thread.daemon = True  # Daemonize the thread (terminate when the main program exits)
    
    depth_thread = threading.Thread(target=run_ros_node, args=(window,DepthSurfaceNode))
    depth_thread.daemon = True  # Daemonize the thread (terminate when the main program exits)
    
    depth_thread.start()
    thruster_thread.start()
    '''
    thrusters = ThrustersSurfaceNode(window = window)
    depth = DepthSurfaceNode(window = window)
    nodelist = [thrusters, depth]
    node_thread = threading.Thread(target=run_multiple_nodes, args=(nodelist,))
    node_thread.daemon = True
    node_thread.start()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()