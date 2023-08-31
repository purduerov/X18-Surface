# Frontend UI for ROV X16
# Written and edited by the X16 Software Team 
# Ethan Burmane (eburmane@purdue.edu), Caden Brennan (brenna51@purdue.edu)
# Last updated: 08/27/2023

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMainWindow()

    def initMainWindow(self):

        # Setting the main window properties
        self.showMaximized()
        self.setWindowTitle("ROV X16")
        self.setStyleSheet('''
            QMainWindow {
                background-color: #2C2C2C;
            }
            ''')

        # Adding the controls dock to the main window
        self.controls_widget = ControlsWidget()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.controls_widget)

        # Adding the readout dock to the main window 
        self.readout_widget = ReadoutWidget()
        self.addDockWidget(Qt.RightDockWidgetArea, self.readout_widget)

        # Adding the stream widget to the main window
        self.setCentralWidget(StreamWidget())

    # This is the event handlers for key press and key release events.
    # This contains the directional control keys and the tool keys.

    def keyPressEvent(self, event):

        # Checking for directional pitch key press events (W, A, S, D)
        if event.key() == Qt.Key_W:
            print("Tilt Forward")
            self.controls_widget.tilt_forward.setDown(True)
            self.controls_widget.tilt_forward.setStyleSheet('''
                QPushButton {
                    background-color: #989898;
                    color: black;
                }
                ''')
            self.controls_widget.tilt_forward.repaint()
        elif event.key() == Qt.Key_A:
            print("Tilt Left")
            self.controls_widget.tilt_left.setDown(True)
            self.controls_widget.tilt_left.setStyleSheet('''
                QPushButton {
                    background-color: #989898;
                    color: black;
                }
                ''')
            self.controls_widget.tilt_left.repaint()
        elif event.key() == Qt.Key_S:
            print("Tilt Backwards")
            self.controls_widget.tilt_backwards.setDown(True)
            self.controls_widget.tilt_backwards.setStyleSheet('''
                QPushButton {
                    background-color: #989898;
                    color: black;
                }
                ''')
            self.controls_widget.tilt_backwards.repaint()
        elif event.key() == Qt.Key_D:
            print("Tilt Right")
            self.controls_widget.tilt_right.setDown(True)
            self.controls_widget.tilt_right.setStyleSheet('''
                QPushButton {
                    background-color: #989898;
                    color: black;
                }
                ''')
            self.controls_widget.tilt_right.repaint()

        # Checking for directional yaw key press events (Q, E)
        elif event.key() == Qt.Key_Q:
            print("Yaw Left")
            self.controls_widget.yaw_left.setDown(True)
            self.controls_widget.yaw_left.setStyleSheet('''
                QPushButton {
                    background-color: #989898;
                    color: black;
                }
                ''')
            self.controls_widget.yaw_left.repaint()
        elif event.key() == Qt.Key_E:
            print("Yaw Right")
            self.controls_widget.yaw_right.setDown(True)
            self.controls_widget.yaw_right.setStyleSheet('''
                QPushButton {
                    background-color: #989898;
                    color: black;
                }
                ''')
            self.controls_widget.yaw_right.repaint()

        # Checking for ascent and descent key press events (R, F)
        elif event.key() == Qt.Key_R:
            print("Ascend")
            self.controls_widget.ascend.setDown(True)
            self.controls_widget.ascend.setStyleSheet('''
                QPushButton {
                    background-color: #989898; 
                    color: black;
                }
                ''')
            self.controls_widget.ascend.repaint()
        elif event.key() == Qt.Key_F:
            print("Descend")
            self.controls_widget.descend.setDown(True)
            self.controls_widget.descend.setStyleSheet('''
                QPushButton {
                    background-color: #989898; 
                    color: black;
                }
                ''')
            self.controls_widget.descend.repaint()

        # Checking for tool key press events (6, 7, 8, 9)
        elif event.key() == Qt.Key_6:
            print("Tool 1")
            self.controls_widget.tool1.setDown(True)
            self.controls_widget.tool1.setStyleSheet('''
                QPushButton {
                    background-color: #989898; 
                    color: black;
                }
                ''')
            self.controls_widget.tool1.repaint()

        elif event.key() == Qt.Key_7:
            print("Tool 2")
            self.controls_widget.tool2.setDown(True)
            self.controls_widget.tool2.setStyleSheet('''
                QPushButton {
                    background-color: #989898; 
                    color: black;
                }
                ''')
            self.controls_widget.tool2.repaint()

        elif event.key() == Qt.Key_8:
            print("Tool 3")
            self.controls_widget.tool3.setDown(True)
            self.controls_widget.tool3.setStyleSheet('''
                QPushButton {
                    background-color: #989898; 
                    color: black;
                }
                ''')
            self.controls_widget.tool3.repaint()

        elif event.key() == Qt.Key_9:
            print("Tool 4")
            self.controls_widget.tool4.setDown(True)
            self.controls_widget.tool4.setStyleSheet('''
                QPushButton {
                    background-color: #989898; 
                    color: black;
                }
                ''')
            self.controls_widget.tool4.repaint()
    
    def keyReleaseEvent(self, event):

        # Checking for directional pitch key release events
        if event.key() == Qt.Key_W:
            self.controls_widget.tilt_forward.setDown(False)
            self.controls_widget.tilt_forward.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.tilt_forward.repaint()
        elif event.key() == Qt.Key_A:
            self.controls_widget.tilt_left.setDown(False)
            self.controls_widget.tilt_left.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.tilt_left.repaint()
        elif event.key() == Qt.Key_S:
            self.controls_widget.tilt_backwards.setDown(False)
            self.controls_widget.tilt_backwards.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }''')
            self.controls_widget.tilt_backwards.repaint()
        elif event.key() == Qt.Key_D:
            self.controls_widget.tilt_right.setDown(False)
            self.controls_widget.tilt_right.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF;
                    color: black;
                }
                ''')
            self.controls_widget.tilt_right.repaint()

        # Checking for directional yaw key release events
        elif event.key() == Qt.Key_Q:
            self.controls_widget.yaw_left.setDown(False)
            self.controls_widget.yaw_left.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.yaw_left.repaint()
        elif event.key() == Qt.Key_E:
            self.controls_widget.yaw_right.setDown(False)
            self.controls_widget.yaw_right.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.yaw_right.repaint()

        # Checking for ascent and descent key release events
        elif event.key() == Qt.Key_R:
            self.controls_widget.ascend.setDown(False)
            self.controls_widget.ascend.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.ascend.repaint()
        elif event.key() == Qt.Key_F:
            self.controls_widget.descend.setDown(False)
            self.controls_widget.descend.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.descend.repaint()

        # Checking for tool key release events
        elif event.key() == Qt.Key_6:
            self.controls_widget.tool1.setDown(False)
            self.controls_widget.tool1.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.tool1.repaint()

        elif event.key() == Qt.Key_7:
            self.controls_widget.tool2.setDown(False)
            self.controls_widget.tool2.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.tool2.repaint()

        elif event.key() == Qt.Key_8:
            self.controls_widget.tool3.setDown(False)
            self.controls_widget.tool3.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.tool3.repaint()

        elif event.key() == Qt.Key_9:
            self.controls_widget.tool4.setDown(False)
            self.controls_widget.tool4.setStyleSheet('''
                QPushButton {
                    background-color: #BFBFBF; 
                    color: black;
                }
                ''')
            self.controls_widget.tool4.repaint()

# This is the stream widget class containing the four streams from the ROV -- 
# three front facing cameras and one bottom facing camera. 

class StreamWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initStream()

    def initStream(self):

        # Setting the stream widget properties
        self.stream = QWidget()
        stream_layout = QGridLayout(self.stream)

        # Creating stream 1 window
        self.stream1 = QLabel("Stream 1")
        self.stream1.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream1, 0, 0)

        # Creating stream 2 window
        self.stream2 = QLabel("Stream 2")
        self.stream2.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream2, 0, 1)

        # Creating stream 3 window
        self.stream3 = QLabel("Stream 3")
        self.stream3.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream3, 1, 0)

        # Creating stream 4 window
        self.stream4 = QLabel("Stream 4")
        self.stream4.setAlignment(Qt.AlignCenter)
        stream_layout.addWidget(self.stream4, 1, 1)

        self.setLayout(stream_layout)

# This is the readout widget class containing the 8 thruster readouts, velocity readout, 
# and depth readout.

class ReadoutWidget(QDockWidget):
    def __init__(self):
        super().__init__()
        self.initReadouts()

    def initReadouts(self):

        # Setting the readout dock properties
        self.setMaximumWidth(300)
        self.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.setAllowedAreas(Qt.RightDockWidgetArea)
        self.setStyleSheet('''
            QDockWidget {
                background-color: transparent;
                border: 0px;
            }
            ''')
        self.readouts = QWidget()
        self.reaout_layout = QGridLayout(self.readouts)
        self.reaout_layout.setSpacing(30)
        self.reaout_layout.setAlignment(Qt.AlignTop)

        # Adding the 8 thruster readouts to the dock
        self.thruster1 = QProgressBar()
        self.thruster1.setMaximumHeight(50)
        self.thruster1.setValue(50)
        self.reaout_layout.addWidget(QLabel("Thruster 1"), 0, 0)
        self.reaout_layout.addWidget(self.thruster1, 0, 1)

        self.thruster2 = QProgressBar()
        self.thruster2.setMaximumHeight(50)
        self.thruster2.setValue(80)
        self.reaout_layout.addWidget(QLabel("Thruster 2"), 1, 0)
        self.reaout_layout.addWidget(self.thruster2, 1, 1)

        self.thruster3 = QProgressBar()
        self.thruster3.setMaximumHeight(50)
        self.thruster3.setValue(20)
        self.reaout_layout.addWidget(QLabel("Thruster 3"), 2, 0)
        self.reaout_layout.addWidget(self.thruster3, 2, 1)

        self.thruster4 = QProgressBar()
        self.thruster4.setMaximumHeight(50)
        self.thruster4.setValue(70)
        self.reaout_layout.addWidget(QLabel("Thruster 4"), 3, 0)
        self.reaout_layout.addWidget(self.thruster4, 3, 1)

        self.thruster5 = QProgressBar()
        self.thruster5.setMaximumHeight(50)
        self.thruster5.setValue(90)
        self.reaout_layout.addWidget(QLabel("Thruster 5"), 4, 0)
        self.reaout_layout.addWidget(self.thruster5, 4, 1)

        self.thruster6 = QProgressBar()
        self.thruster6.setMaximumHeight(50)
        self.thruster6.setValue(10)
        self.reaout_layout.addWidget(QLabel("Thruster 6"), 5, 0)
        self.reaout_layout.addWidget(self.thruster6, 5, 1)

        self.thruster7 = QProgressBar()
        self.thruster7.setMaximumHeight(50)
        self.thruster7.setValue(30)
        self.reaout_layout.addWidget(QLabel("Thruster 7"), 6, 0)
        self.reaout_layout.addWidget(self.thruster7, 6, 1)

        self.thruster8 = QProgressBar()
        self.thruster8.setMaximumHeight(50)
        self.thruster8.setValue(60)
        self.reaout_layout.addWidget(QLabel("Thruster 8"), 7, 0)
        self.reaout_layout.addWidget(self.thruster8, 7, 1)

        # Adding the velocity readout to the dock
        self.velocity = QLCDNumber()
        self.velocity.setMaximumSize(100, 100)
        self.velocity.setDigitCount(5)
        self.velocity.display(5.3)
        self.reaout_layout.addWidget(QLabel("Velocity"), 8, 0)
        self.reaout_layout.addWidget(self.velocity, 8, 1)

        # Adding the depth readout to the dock
        self.depth = QLCDNumber()
        self.depth.setMaximumSize(100, 100)
        self.depth.setDigitCount(5)
        self.depth.display(12.6)
        self.reaout_layout.addWidget(QLabel("Depth"), 9, 0)
        self.reaout_layout.addWidget(self.depth, 9, 1)

        self.setWidget(self.readouts)        

# This is the controls widget class containing the directional tilt buttons, directional yaw buttons, 
# ascent and descent buttons, and tool buttons.

class ControlsWidget(QDockWidget):
    def __init__(self):
        super().__init__()
        self.initControls()

    def initControls(self):

        # Setting the controls dock properties
        self.setMaximumSize(300, 300)
        self.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.setStyleSheet('''
            QDockWidget {
                background-color: transparent;
                border: 0px;
            }
            ''')
        self.controls = QWidget()
        self.controls_layout = QGridLayout(self.controls)

        # Creating directional tilt buttons
        self.tilt_forward = QPushButton("W\nPitch\nForward")
        self.tilt_forward.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tilt_forward.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tilt_forward, 0, 1)

        self.tilt_left = QPushButton("A\nPitch\nLeft")
        self.tilt_left.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tilt_left.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tilt_left, 1, 0)

        self.tilt_backwards = QPushButton("S\nPitch\nBackwards")
        self.tilt_backwards.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tilt_backwards.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tilt_backwards, 1, 1)

        self.tilt_right = QPushButton("D\nPitch\nRight")    
        self.tilt_right.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tilt_right.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tilt_right, 1, 2)

        # Creating directional yaw buttons 
        self.yaw_left = QPushButton("Q\nYaw\nLeft")
        self.yaw_left.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.yaw_left.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.yaw_left, 0, 0)

        self.yaw_right = QPushButton("E\nYaw\nRight")
        self.yaw_right.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.yaw_right.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.yaw_right, 0, 2)

        # Creating the ascent and descent buttons
        self.ascend = QPushButton("R\nAscend\n")
        self.ascend.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.ascend.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.ascend, 0, 3)

        self.descend = QPushButton("F\nDescend\n")
        self.descend.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.descend.setMaximumSize(100, 70)  
        self.controls_layout.addWidget(self.descend, 1, 3)      

        # Creating a spacer between the directional and tool buttons
        self.spacer = QSpacerItem(100, 70)
        self.controls_layout.addItem(self.spacer, 2, 0)

        # Creating tools buttons 
        self.tool1 = QPushButton("6\nTool")
        self.tool1.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tool1.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tool1, 3, 0)

        self.tool2 = QPushButton("7\nTool")
        self.tool2.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tool2.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tool2, 3, 1)

        self.tool3 = QPushButton("8\nTool")
        self.tool3.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tool3.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tool3, 3, 2)

        self.tool4 = QPushButton("9\nTool")
        self.tool4.setStyleSheet('''
            QPushButton { 
                background-color: #BFBFBF; 
                color: black;
            }
            ''')
        self.tool4.setMaximumSize(100, 70)
        self.controls_layout.addWidget(self.tool4, 3, 3)

        self.setWidget(self.controls)
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec()
