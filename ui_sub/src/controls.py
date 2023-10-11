#!/usr/bin/env python3
# This is the controls widget class containing the directional tilt buttons, directional yaw buttons, 
# ascent and descent buttons, and tool buttons.

# (if using avahi, ignore below statement)
# To port the camera streams, you will need to configure your IP address to remain static.

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ControlsWidget(QDockWidget):
    def __init__(self):
        super().__init__()
        self.initControls()

    def initControls(self):

        # setting the controls dock properties
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

        # creating directional tilt buttons
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

        # creating directional yaw buttons 
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

        # creating the ascent and descent buttons
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

        # creating a spacer between the directional and tool buttons
        self.spacer = QSpacerItem(100, 70)
        self.controls_layout.addItem(self.spacer, 2, 0)

        # creating tools buttons 
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