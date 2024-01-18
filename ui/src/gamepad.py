import subprocess

gamepad_connect_cmd = "ros2 run gamepad sender.py"


class gamepad:
    def __init__(self, connection):
        self.gamepad_process = None
        self.connection = False
        self.ssh_connection = connection

    def start(self):
        if self.ssh_connection is None:
            print("ERROR: gamepad unable to connect")
            return

        print("Connecting to the gamepad...")
        self.gamepad_process = subprocess.Popen(
            gamepad_connect_cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if self.gamepad_process is not None:
            print(f"Process {self.gamepad_process.pid} started")
        else:
            print("Failed to connect to the gamepad")

    def stop(self):
        if self.gamepad_process is not None:
            self.gamepad_process.kill()
            print(f"Process {self.gamepad_process.pid} killed")
