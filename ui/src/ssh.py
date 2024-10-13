import paramiko
import os
from dotenv import load_dotenv
import time

load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")

# # TODO
#     # Make closing a function
#     # Function for establishing camera stream connections
#     # Function for Gamepad Connections


class Ssh:

    def __init__(self, node):
        self.ssh_hostname = os.getenv("HOST_IP")  # The IP address of the PI
        print(self.ssh_hostname)
        self.ssh_password = os.getenv("HOST_PASSWORD")  # The Password of the PI
        print(self.ssh_password)
        self.ssh_username = os.getenv("HOST_USERNAME")  # The username of the PI
        print(self.ssh_username)

        self.ssh_client = None  # Variable for the SSH client object
        self.connection = None  # Variable for checking if connection is present
        self.node = node

    def connect(self):

        try:
            self.ssh_client = paramiko.SSHClient()
            # Add device to known hosts so it can connect.
            # if not present gives error - AttributeError: 'NoneType' object has no attribute 'time'
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the host
            self.ssh_client.connect(
                self.ssh_hostname,
                username=self.ssh_username,
                password=self.ssh_password,
            )
            if self.ssh_client is not None:
                self.node.get_logger().info("SSH Connection Established")

                print("SSH Connection Established")
                self.connection = True
                self.ssh_client.exec_command("ls")
            else:
                print("ERROR: SSH Connection Failed")

        except Exception as e:
            print(f"ERROR: {e}")

    def close(self):

        # This is a program to stop ros2 and more

        # if self.ssh_client is not None:
        #     self.ssh_client.exec_command(
        #         "ps aux | grep ros2 | awk '{print $2}' | xargs kill -9 && tmux kill-session -t ros2_session")

        # closing the ssh connection
        if self.ssh_client is not None:
            self.ssh_client.close()
            print("SSH connection closed")


###############################
### Testing File Code Below ###
###############################

# def main():
#     ssh = Ssh()
#     ssh.connect()
#     time.sleep(10)
#     ssh.close()


# if __name__ == "__main__":
#     main()
