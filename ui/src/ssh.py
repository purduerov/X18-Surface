import paramiko
import socket
import time 

class controller():
    def __init__(self):
        self.ssh_host = "10.0.0.102"
        self.ssh_username = "pi"
        self.ssh_password = "pie"
        self.ssh_client = None
        self.pid_list = list()

    def get_ip(self):
        try:
            hostname = socket.gethostname()
            ip = "10.0.0.10" + socket.gethostbyname(socket.gethostname()).split('.')[-1]
            print("Local IP address: ", ip)
            return ip
        
        except Exception as e:
            print(f"Error: {e}")

    def connect(self):
        try:
            ip = self.get_ip()
            stream1_launch_cmd = (f"gst-launch-1.0 -v v4l2src device=/dev/video8 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host={ip} port=5600 sync=false buffer-size=1048576 & echo $! > pid.txt")
            stream2_launch_cmd = (f"gst-launch-1.0 -v v4l2src device=/dev/video4 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host={ip} port=5601 sync=false buffer-size=1048576 & echo $! > pid.txt")

            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.ssh_host, username=self.ssh_username, password=self.ssh_password)
            if self.ssh_client is not None:
                print("SSH connection established")
            else:
                print("SSH connection failed")
                # TODO: handle this error

            print("Launching camera stream 1...")
            self.ssh_client.exec_command(stream1_launch_cmd)
            time.sleep(1)
            __, stdout, __ = self.ssh_client.exec_command("cat pid.txt")
            self.pid = stdout.read().decode("utf-8").strip()
            self.pid_list.append(self.pid)
            print(f"Process {self.pid} started")

            print("Launching camera stream 2...")
            self.ssh_client.exec_command(stream2_launch_cmd)
            time.sleep(1)
            __, stdout, __ = self.ssh_client.exec_command("cat pid.txt")
            self.pid = stdout.read().decode("utf-8").strip()
            self.pid_list.append(self.pid)
            print(f"Process {self.pid} started")
            
        except Exception as e:
            print(f"Error: {e}")

    def close(self):
        if self.pid_list is not None:
            for pid in self.pid_list:
                self.ssh_client.exec_command("kill " + pid)
                print(f"Process {pid} killed")

        if self.ssh_client is not None:
            self.ssh_client.close()
            print("SSH connection closed")

            








