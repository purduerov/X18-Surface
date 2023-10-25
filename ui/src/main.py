# Frontend UI for ROV X16
# Written and edited by the X16 Software Team 
# Last updated: 09/27/2023

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import command as command
import subprocess as subprocess

import readouts as readouts
import controls as controls 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        screen_geometry = QDesktopWidget().screenGeometry()
        screen_height = screen_geometry.height()
        screen_width = screen_geometry.width()
        self.setGeometry(0, screen_height // 2, screen_width, screen_height // 2)
        self.setWindowTitle("ROV X16")
        self.setStyleSheet("background-color: #2C2C2C;") # keeping the border for size estimation "border: 1px solid black;"
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        grid_layout = QGridLayout()

        self.thrusters_widget = readouts.ThrustersWidget()
        self.thrusters_widget.setMaximumSize(300, 300)
        grid_layout.addWidget(self.thrusters_widget, 0, 0, 2, 1)

        self.velocity_widget = readouts.VelocityWidget()
        self.velocity_widget.setMaximumSize(150, 500)
        grid_layout.addWidget(self.velocity_widget, 0, 1, 2, 1)
    
        self.depth_widget = readouts.DepthWidget()
        self.depth_widget.setMaximumSize(150, 500)
        grid_layout.addWidget(self.depth_widget, 0, 2, 1, 1)

        self.fine_widget = readouts.FineModeWidget()
        self.fine_widget.setMaximumSize(150, 500)
        grid_layout.addWidget(self.fine_widget, 1, 2, 1, 1)

        main_widget.setLayout(grid_layout)

if __name__ == "__main__":
    python_executable = sys.executable
    subprocess.Popen([python_executable, "ui/src/ssh_startup.py"])
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec()
