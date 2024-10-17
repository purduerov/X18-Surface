import signal
import time
import rclpy


class SignalHandler:
    def __init__(self, node, rov_connection, camera_streams):
        self.node = node
        self.rov_connection = rov_connection
        self.camera_streams = camera_streams
        self.shutdown = None
        

    def close_application(self, signal, frame):
        """
        Closing the application
        Triggered when the user presses Ctrl+C
        Camera streams are closed and the SSH connection is closed
        """

        if self.shutdown:
            return
        self.shutdown = True
        
        try:
            if self.node is not None:
                self.node.get_logger().info("Closing application...")  
            
            if self.camera_streams is True:
                result = self.camera_streams.close_camera_streams()
                if result is False:
                    if self.node is not None:
                        self.node.get_logger().error("Trying again...")
                    result = self.camera_streams.close_camera_streams()

            if self.rov_connection is not None:
                self.rov_connection.close()
            
            if self.node is not None:
                self.node.destroy_node()

            rclpy.shutdown()
            
        except Exception as e:
            if self.node is not None:
                self.node.get_logger().error("Error during shutdown: " + str(e))
        
        print("Application closed")
        exit(0)
    