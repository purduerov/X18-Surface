#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from interface import Ui_MainWindow
from ssh import ssh
from streams import streams
from gamepad import gamepad

class MainWindow(QMainWindow):
    def __init__(self, ssh_comm):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ssh = ssh_comm
        # setting general window properties
        self.setWindowTitle("ROX X16")
        screen_geometry = QDesktopWidget().screenGeometry()
        screen_height = screen_geometry.height()
        screen_width = screen_geometry.width()
        self.setGeometry(0, screen_height // 2, screen_width, screen_height // 2)
        self.setMaximumSize(screen_width, screen_height // 2)
        self.setMinimumSize(screen_width, screen_height // 2)
            
    def closeEvent(self, event):
        confirmation = QMessageBox.question(
            self,
            "Exit",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if confirmation == QMessageBox.Yes:
            #streams.stop()
            # gamepad.stop()
            #ssh_comm = ssh()
            self.ssh.close()
            print("Closing application")
            event.accept()
        else:
            event.ignore()