# Frontend UI for ROV X16
# Written and edited by the X16 Software Team 
# Last updated: 09/27/2023

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import command as command

import streams as stream
import readouts as readouts
import controls as controls 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting the main window properties
        self.showMaximized()
        self.setWindowTitle("ROV X16")
        self.setStyleSheet('''
            QMainWindow {
                background-color: #2C2C2C;
            }
            ''')

        # adding the controls dock to the main window
        self.controls_widget = controls.ControlsWidget()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.controls_widget)

        # adding the readout dock to the main window 
        self.readout_widget = readouts.ReadoutsWidget()
        self.addDockWidget(Qt.RightDockWidgetArea, self.readout_widget)
        
        # adding the stream widget to the main window
        self.camera_stream_widget = stream.CameraStreamWidget()
        self.setCentralWidget(self.camera_stream_widget)

    # This is the event handlers for key press and key release events.
    # This contains the directional control keys and the tool keys.

    def keyPressEvent(self, event):

        # checking for directional pitch key press events (W, A, S, D)
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

        # checking for directional yaw key press events (Q, E)
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

        # checking for ascent and descent key press events (R, F)
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

        # checking for tool key press events (6, 7, 8, 9)
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

        # checking for directional pitch key release events
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

        # checking for directional yaw key release events
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

        # checking for tool key release events
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

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec()
