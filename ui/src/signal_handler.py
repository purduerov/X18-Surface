import signal
import time
import rclpy

class SignalHandler:
    def __init__(self, node, rov_connection, cam_streams):
        self.node = node
        self.rov_connection = rov_connection
        self.cam_streams = cam_streams
        self.shutdown = None
        

    def handler(self, signal, frame):
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
                self.node.get_logger().info("Closing application")  
            
            if self.cam_streams is not None:
                self.cam_streams.close_camera_streams()
                if self.node is not None:
                    self.node.get_logger().info("Camera streams closed")

            if self.rov_connection is not None:
                self.rov_connection.close()
                if self.node is not None:
                    self.node.get_logger().info("Connection to ROV closed")
            
            if self.node is not None:
                self.node.destroy_node()

            rclpy.shutdown()
            
        except Exception as e:
            if self.node is not None:
                self.node.get_logger().error("Error during shutdown: " + str(e))
        
        print("Application closed")
        exit(0)
        
    #######
    #Chat GPT Closure code
    #def __init__(self, data):
    #    self.data = data

    #def handler(self, signum, frame):
    #    print(f"Signal {signum} received with data: {self.data}")
    #    self.data = "Data updated after signal"
    #####