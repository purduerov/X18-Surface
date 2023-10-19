# Frontend UI for ROV X16
# Written and edited by the X16 Software Team 
# Last updated: 09/27/2023

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import command as command
import subprocess as subprocess

import streams as stream
import readouts as readouts
import controls as controls 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.setWindowTitle("ROV X16")
        self.setStyleSheet('''
            QMainWindow {
                background-color: #2C2C2C;
            }
            ''')
        
        # self.controls_widget = controls.ControlsWidget()
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.controls_widget)

        self.readout_widget = readouts.ReadoutsWidget()
        self.addDockWidget(Qt.RightDockWidgetArea, self.readout_widget)
        
        self.camera_stream_widget = stream.CameraStreamWidget()
        self.setCentralWidget(self.camera_stream_widget)

if __name__ == "__main__":
    python_executable = sys.executable
    subprocess.Popen([python_executable, "ui/src/ssh_startup.py"])
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec()
