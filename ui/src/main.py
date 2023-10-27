#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from interface import Ui_MainWindow
from ssh import controller
from streams import streams

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        screen_geometry = QDesktopWidget().screenGeometry()
        screen_height = screen_geometry.height()
        screen_width = screen_geometry.width()
        self.setGeometry(0, screen_height // 2, screen_width, screen_height // 2)

    def closeEvent(self, event):
        confirmation = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            streams.stop()
            controller.close()
            event.accept()
        else:
            event.ignore()
        
if __name__ == "__main__":
    controller = controller()
    controller.connect()

    streams = streams()
    streams.start()

    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec()

