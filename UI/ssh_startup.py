import paramiko

ssh_host = "10.0.0.4"
ssh_port = 22
ssh_username = "pi"
ssh_password = "pie"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

command_to_execute = (
    "gst-launch-1.0 -v v4l2src device=/dev/video8 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.103 port=5600 sync=false buffer-size=1048576"
    "gst-launch-1.0 -v v4l2src device=/dev/video4 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.103 port=5601 sync=false buffer-size=1048576"
)

try: 
    ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)
    stdin, stdout, stderr = ssh_client.exec_command(command_to_execute)
    ssh_client.close()
except Exception as e:
    print(f"Error: {e}")


