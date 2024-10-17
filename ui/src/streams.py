import time


class Streams:

    def __init__(self, node, rov_connection):
        self.node = node
        self.rov_connection = rov_connection
        self.attempted = False


    def run_camera_streams(self):
        """
        Starts the camera streams on the ROV
        Returns a boolean indicating if the camera streams started successfully
        """
        # check if the camera streams are already running
        __, stdout, __ = self.rov_connection.exec_command("ps aux | grep mediamtx")
        response = stdout.read().decode("utf-8")
        if "./mediamtx" in response:
            self.node.get_logger().info("Camera streams already running")
            return True

        self.node.get_logger().info("Starting camera streams...")
        self.rov_connection.exec_command("cd cameras2 && nohup ./mediamtx >> /dev/null 2>&1 &")

        # check if the camera streams are running
        __, stdout, __ = self.rov_connection.exec_command("ps aux | grep mediamtx")
        response = stdout.read().decode("utf-8") 
        if "./mediamtx" not in response:
            if self.attempted == False:
                self.attempted = True
                self.node.get_logger().warning("Trying again...")
                time.sleep(5)
                self.run_camera_streams()
            else:
                self.node.get_logger().error("Camera streams failed to start")
                return False

        self.node.get_logger().info("Camera streams started")
        self.node.get_logger().warning("Camera streams can take a few minutes to start")
        return True


    def close_camera_streams(self):
        """
        Closes the camera streams on the ROV
        Returns a boolean indicating if the camera streams closed successfully
        """
        self.node.get_logger().info("Closing camera streams...")
        self.rov_connection.exec_command("killall mediamtx")

        # check if the camera streams are closed
        __, stdout, __ = self.rov_connection.exec_command("ps aux | grep mediamtx")
        response = stdout.read().decode("utf-8")
        if "./mediamtx" in response:
            self.node.get_logger().warning("Camera streams failed to close")
            return False

        self.node.get_logger().info("Camera streams closed")
        return True
