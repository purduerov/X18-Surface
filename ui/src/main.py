from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import subprocess as subprocess
import command as command
from x16frontend import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        screen_geometry = QDesktopWidget().screenGeometry()
        screen_height = screen_geometry.height()
        screen_width = screen_geometry.width()

        self.setGeometry(0, screen_height // 2, screen_width, screen_height // 2)
        
if __name__ == "__main__":
    # python_executable = sys.executable
    # subprocess.Popen([python_executable, "ui/src/ssh_startup.py"])
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec()
