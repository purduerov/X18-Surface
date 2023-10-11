#!/usr/bin/env python3
# This is the readout widget class for the X16 ROV 
# This contains the 8 thruster readouts, velocity readout, and depth readout.

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ReadoutsWidget(QDockWidget):
    def __init__(self):
        super().__init__()
        self.initReadouts()

    def initReadouts(self):

        # setting the readout dock properties
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

        # adding the 8 thruster readouts to the dock
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

        # adding the velocity readout to the dock
        self.velocity = QLCDNumber()
        self.velocity.setMaximumSize(100, 100)
        self.velocity.setDigitCount(5)
        self.velocity.display(5.3)
        self.reaout_layout.addWidget(QLabel("Velocity"), 8, 0)
        self.reaout_layout.addWidget(self.velocity, 8, 1)

        # adding the depth readout to the dock
        self.depth = QLCDNumber()
        self.depth.setMaximumSize(100, 100)
        self.depth.setDigitCount(5)
        self.depth.display(12.6)
        self.reaout_layout.addWidget(QLabel("Depth"), 9, 0)
        self.reaout_layout.addWidget(self.depth, 9, 1)

        self.setWidget(self.readouts)        