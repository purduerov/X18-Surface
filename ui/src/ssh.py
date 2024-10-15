import paramiko
import os
import netifaces
from dotenv import load_dotenv
import time

load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")

# # TODO 
#     # Make closing a function
#     # Function for establishing camera stream connections 
#     # Function for Gamepad Connections


class Ssh:

    def __init__(self, node):
        self.ssh_hostname = os.getenv("HOST_IP") # The IP address of the PI
        self.ssh_password = os.getenv("HOST_PASSWORD") # The Password of the PI
        self.ssh_username = os.getenv("HOST_USERNAME") # The username of the PI

        self.ssh_client = None # Variable for the SSH client object
        self.node = node

        
    def connect(self):
        
        try:
            # getting the local ip address
            ip = self.get_ip()
            print(f"Local IP address: {ip}")
            
            self.ssh_client = paramiko.SSHClient()
            # Add device to known hosts so it can connect.
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the host
            self.ssh_client.connect(self.ssh_hostname, username=self.ssh_username, password=self.ssh_password)
            if self.ssh_client is not None: 
                self.node.get_logger().info("SSH Connection Established")
                print("SSH Connection Established")
                return self.ssh_client
            else:
                self.node.get_logger().info("SSH Connection Failed")
                print("ERROR: SSH Connection Failed")
                return None
        
        except Exception as e:
            self.node.get_logger().info(f"ERROR: {e}")
            print(f"ERROR: {e}")

    def get_ip(self):
        try:
            interfaces = netifaces.interfaces()
            for interface in interfaces:
                addrs = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addrs:
                    for addr_info in addrs[netifaces.AF_INET]:
                        ip_address = addr_info["addr"]
                        if ip_address.startswith("192.168.1."):
                            return ip_address
        except Exception as e:
            print(f"ERROR: {e}")

    
    def close(self):
        # closing the ssh connection
        if self.ssh_client is not None:
            self.ssh_client.close()
            print("SSH connection closed")
            self.node.get_logger().info("SSH Connection Closed")



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


        