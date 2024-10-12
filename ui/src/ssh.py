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
        print(self.ssh_hostname)
        self.ssh_password = os.getenv("HOST_PASSWORD") # The Password of the PI
        print(self.ssh_password)
        self.ssh_username = os.getenv("HOST_USERNAME") # The username of the PI
        print(self.ssh_username)

        self.ssh_client = None # Variable for the SSH client object
        self.connection = None # Variable for checking if connection is present
        self.node = node

        
    def connect(self):
        
        try:
            # getting the local ip address
            ip = self.get_ip()
            print(f"Local IP address: {ip}")
            #ros_id = 69
            # commands to launch on the pi
            ros2_source_cmd = "source ~/.bashrc >> ~/ros2_ws/startup_logs/sourcebash.txt && export ROS_DOMAIN_ID=69 && source ros2_ws/install/setup.bash >> ~/ros2_ws/startup_logs/source.txt && echo $ROS_DOMAIN_ID >> ~/ros2_ws/startup_logs/domain_id_tmux"
            #ros2_launch_cmd = "ros2 launch rov_launch run_rov_launch.xml >> ~/ros2_ws/startup_logs/launch.txt"
            stream1_launch_cmd = f"gst-launch-1.0 -v v4l2src device={self.device_name1} ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host={ip} port=5600 sync=false buffer-size=1048576 & echo $! > pid.txt"
            stream2_launch_cmd = f"gst-launch-1.0 -v v4l2src device={self.device_name2} ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host={ip} port=5601 sync=false buffer-size=1048576 & echo $! > pid.txt"
            stream3_launch_cmd = f"gst-launch-1.0 -v v4l2src device={self.device_name3} ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host={ip} port=5602 sync=false buffer-size=1048576 & echo $! > pid.txt"
            stream4_launch_cmd = f"gst-launch-1.0 -v v4l2src device={self.device_name4} ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host={ip} port=5603 sync=false buffer-size=1048576 & echo $! > pid.txt"

            self.ssh_client = paramiko.SSHClient()
            # Add device to known hosts so it can connect.
            # if not present gives error - AttributeError: 'NoneType' object has no attribute 'time'
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the host
            self.ssh_client.connect(self.ssh_hostname, username=self.ssh_username, password=self.ssh_password)
            if self.ssh_client is not None: 
                self.node.get_logger().info("SSH Connection Established")

                print("SSH Connection Established")
                self.connection = True
                self.ssh_client.exec_command("ls")
            else:
                print("ERROR: SSH Connection Failed")

            # launching the camera streams on the pi
            self.launch_stream(1, stream1_launch_cmd)
            self.launch_stream(2, stream2_launch_cmd)
            self.launch_stream(3, stream3_launch_cmd)
            self.launch_stream(4, stream4_launch_cmd)

            return self.connection
                
        except Exception as e:
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


        