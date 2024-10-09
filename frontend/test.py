import paramiko
import os
from dotenv import load_dotenv
import time

# SSH details
hostname = "192.168.1.4"
username = "pi"
password = "pie"

# TODO 
    # Make closing a function
    # Function for establishing camera stream connections 
    # Function for Gamepad Connections

# Create an SSH client
ssh_client = paramiko.SSHClient()
# Add device to known hosts so it can connect.
# if not present gives error - AttributeError: 'NoneType' object has no attribute 'time'
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the host
    ssh_client.connect(hostname, username=username, password=password)

    # Execute a command
    stdin, stdout, stderr = ssh_client.exec_command('ls')

    # Print the output
    print(stdout.read().decode())
finally:
    # Always close the SSH client explicitly
    ssh_client.close()


class Ssh:
    def __init__(self):
        self.ssh_hostname = os.getenv("HOST_IP") # The IP address of the PI
        self.ssh_password = os.getenv("HOST_PASSWORD") # The Password of the PI
        self.ssh_username = os.getenv("HOST_USERNAME") # The username of the PI
        self.ssh_client = None # Variable for the SSH client
        self.connection = None # 

        
    def connect(self):
        try:
            # Create an SSH client
            ssh_client = paramiko.SSHClient()
            # Add device to known hosts so it can connect.
            # if not present gives error - AttributeError: 'NoneType' object has no attribute 'time'
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the host
            ssh_client.connect(self.ssh_hostname, username=self.ssh_username, password=self.ssh_password)

            if self.ssh_client is not None: 
                print("SSH Connection Established")
                self.connection = True
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


def main():
    ssh = Ssh()
    ssh.connect()
    time.sleep(10)
    ssh.close()

if __name__ == "__main__":
    main()


        