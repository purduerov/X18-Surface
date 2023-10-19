import paramiko

# SSH credentials
ssh_host = "10.0.0.4"
ssh_username = "pi"
ssh_password = "pie"

# Command to execute on the Raspberry Pi
command1_to_execute = (
    "gst-launch-1.0 -v v4l2src device=/dev/video8 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.101 port=5600 sync=false buffer-size=1048576"
)

command2_to_execute = (
    "gst-launch-1.0 -v v4l2src device=/dev/video4 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.101 port=5601 sync=false buffer-size=1048576"
)

try:
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the Raspberry Pi
    ssh_client.connect(ssh_host, username=ssh_username, password=ssh_password)

    # Execute the SSH command
    stdin, stdout, stderr = ssh_client.exec_command(command1_to_execute)
    # stdin, stdout, stderr = ssh_client.exec_command(f"nohup {command2_to_execute} &")

    print("Standard Output:")
    print(stdout.read().decode('utf-8'))

    # Close the SSH connection
    ssh_client.close()

except Exception as e:
    print(f"Error: {e}")