from paramiko import SSHClient, AutoAddPolicy
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")


class Ssh:

    def __init__(self, node):
        self.ssh_hostname = os.getenv("ROV_IP") # The IP address of the Pi
        self.ssh_password = os.getenv("ROV_PASSWORD") # The password of the Pi
        self.ssh_username = os.getenv("ROV_USERNAME") # The username of the Pi
        self.rov_connection = None 
        self.node = node

        
    def connect(self):
        """
        Establishes an SSH connection to the ROV
        Returns the SSH client object
        """
        
        try:
            self.rov_connection = SSHClient()
            # add device to known hosts so it can connect
            self.rov_connection.set_missing_host_key_policy(AutoAddPolicy())
            self.rov_connection.connect(self.ssh_hostname, username=self.ssh_username, password=self.ssh_password)
            if self.rov_connection is not None: 
                self.node.get_logger().info("SSH connection established") 
                return self.rov_connection
            else:
                self.node.get_logger().error("SSH connection failed")
                return None

        except Exception as e:
            self.node.get_logger().error(f"ERROR: {e}")
            print(f"ERROR: {e}")
            return None

    
    def close(self):
        """
        Closes the SSH connection to the ROV
        """
        if self.rov_connection is not None:
            self.rov_connection.close()
            self.node.get_logger().info("ROV connection closed")

        