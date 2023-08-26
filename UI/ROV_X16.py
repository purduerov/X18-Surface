import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMainWindow()

    def initMainWindow(self):

        # setting the main window properties
        self.showMaximized()
        self.setWindowTitle("ROV X16")

        # adding the controls dock to the main window
        self.controls_widget = ControlsWidget()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.controls_widget)

        # adding the readout dock to the main window 
        self.readout_widget = ReadoutWidget()
        self.addDockWidget(Qt.RightDockWidgetArea, self.readout_widget)

        # adding the stream widget to the main window
        self.setCentralWidget(StreamWidget())
        
    # def controlsEvent(self, event):
    #     key = event.key()
    #     if key == Qt.Key_W:
    #         print("Forward")
    #     elif key == Qt.Key_A:
    #         print("Left")
    #     elif key == Qt.Key_S:
    #         print("Backward")
    #     elif key == Qt.Key_D:
    #         print("Right")

class StreamWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initStream()

    def initStream(self):

        # setting the stream widget properties
        stream = QWidget()
        stream_layout = QGridLayout(stream)

        # creating stream 1 window
        self.stream1 = QLabel("Stream 1")
        self.stream1.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream1, 0, 0)

        # creating stream 2 window
        self.stream2 = QLabel("Stream 2")
        self.stream2.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream2, 0, 1)

        # creating stream 3 window
        self.stream3 = QLabel("Stream 3")
        self.stream3.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream3, 1, 0)

        # creating stream 4 window
        self.stream4 = QLabel("Stream 4")
        self.stream4.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream4, 1, 1)

        self.setLayout(stream_layout)

class ReadoutWidget(QDockWidget):
    def __init__(self):
        super().__init__()
        self.initReadouts()

    def initReadouts(self):

        # setting the readout dock properties
        self.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        readouts = QWidget()
        readout_layout = QGridLayout(readouts)

        # adding the 8 thruster readouts to the dock
        self.thruster1 = QProgressBar()
        self.thruster1.setMaximumHeight(50)
        self.thruster1.setValue(50)
        readout_layout.addWidget(QLabel("Thruster 1"), 0, 0)
        readout_layout.addWidget(self.thruster1, 0, 1)

        self.thruster2 = QProgressBar()
        self.thruster2.setMaximumHeight(50)
        self.thruster2.setValue(80)
        readout_layout.addWidget(QLabel("Thruster 2"), 1, 0)
        readout_layout.addWidget(self.thruster2, 1, 1)

        self.thruster3 = QProgressBar()
        self.thruster3.setMaximumHeight(50)
        self.thruster3.setValue(20)
        readout_layout.addWidget(QLabel("Thruster 3"), 2, 0)
        readout_layout.addWidget(self.thruster3, 2, 1)

        self.thruster4 = QProgressBar()
        self.thruster4.setMaximumHeight(50)
        self.thruster4.setValue(70)
        readout_layout.addWidget(QLabel("Thruster 4"), 3, 0)
        readout_layout.addWidget(self.thruster4, 3, 1)

        self.thruster5 = QProgressBar()
        self.thruster5.setMaximumHeight(50)
        self.thruster5.setValue(90)
        readout_layout.addWidget(QLabel("Thruster 5"), 4, 0)
        readout_layout.addWidget(self.thruster5, 4, 1)

        self.thruster6 = QProgressBar()
        self.thruster6.setMaximumHeight(50)
        self.thruster6.setValue(10)
        readout_layout.addWidget(QLabel("Thruster 6"), 5, 0)
        readout_layout.addWidget(self.thruster6, 5, 1)

        self.thruster7 = QProgressBar()
        self.thruster7.setMaximumHeight(50)
        self.thruster7.setValue(30)
        readout_layout.addWidget(QLabel("Thruster 7"), 6, 0)
        readout_layout.addWidget(self.thruster7, 6, 1)

        self.thruster8 = QProgressBar()
        self.thruster8.setMaximumHeight(50)
        self.thruster8.setValue(60)
        readout_layout.addWidget(QLabel("Thruster 8"), 7, 0)
        readout_layout.addWidget(self.thruster8, 7, 1)

        # adding the velocity readout to the dock
        self.velocity = QLCDNumber()
        self.velocity.setMaximumSize(100, 100)
        self.velocity.setDigitCount(5)
        self.velocity.display(5.3)
        readout_layout.addWidget(QLabel("Velocity"), 8, 0)
        readout_layout.addWidget(self.velocity, 8, 1)

        # adding the depth readout to the dock
        self.depth = QLCDNumber()
        self.depth.setMaximumSize(100, 100)
        self.depth.setDigitCount(5)
        self.depth.display(12.6)
        readout_layout.addWidget(QLabel("Depth"), 9, 0)
        readout_layout.addWidget(self.depth, 9, 1)

        self.setWidget(readouts)        

class ControlsWidget(QDockWidget):
    def __init__(self):
        super().__init__()
        self.initControls()

    def initControls(self):

        # setting the controls dock properties
        self.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        controls = QWidget()
        controls_layout = QGridLayout(controls)

        # creating cmovement buttons
        self.forward = QPushButton("W")
        self.left = QPushButton("A")
        self.backwards = QPushButton("S")
        self.right = QPushButton("D")    

        # mapping buttons to the dock
        controls_layout.addWidget(self.forward, 0, 1)
        controls_layout.addWidget(self.left, 1, 0)
        controls_layout.addWidget(self.backwards, 1, 1)
        controls_layout.addWidget(self.right, 1, 2)

        self.setWidget(controls)

        # # connecting button press and release events to signal
        # self.forward.pressed.connect(lambda: self.keyStateChanged.emit('forward', True))
        # self.forward.released.connect(lambda: self.keyStateChanged.emit('forward', False))
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec()
