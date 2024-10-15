
class Streams:
    def __init__(self, ssh_client):
        self.ssh_client = ssh_client
    
    def run_camera_streams(self):
        # Running the ssh client 
        # Run the mediamtx command
        self.ssh_client.exec_command("cd cameras2/")
        self.ssh_client.exec_command("./mediamtx")

        ### Code NOT TESTED ###

    