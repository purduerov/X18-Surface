# This is the readout widget class for the X16 ROV 
# This contains the 8 thruster readouts, velocity readout, and depth readout.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ThrustersWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initThrusters()

    def initThrusters(self):
        self.thrusters_layout = QGridLayout(self)
        self.thrusters_layout.setSpacing(30)
        self.setMaximumSize(300, 500)
        self.setStyleSheet("background: transparent;")
        self.setLayout(self.thrusters_layout)

        self.thruster_label = QLabel("Thrusters")
        self.thruster_label.setAlignment(Qt.AlignCenter)
        self.thrusters_layout.addWidget(self.thruster_label, 0, 0, 1, 4)
        self.thruster_label.setMaximumHeight(20)

        self.top_label = QLabel("Top")
        self.top_label.setAlignment(Qt.AlignCenter)
        self.thrusters_layout.addWidget(self.top_label, 1, 0, 1, 2)
        self.top_label.setMaximumHeight(20)

        self.bottom_label = QLabel("Bottom")
        self.bottom_label.setAlignment(Qt.AlignCenter)
        self.thrusters_layout.addWidget(self.bottom_label, 1, 2, 1, 2)
        self.bottom_label.setMaximumHeight(20)

        self.top_front_left = QProgressBar()
        self.top_front_left.setMaximumHeight(20)
        self.top_front_left.setValue(0)
        self.thrusters_layout.addWidget(QLabel("FL"), 2, 0)
        self.thrusters_layout.addWidget(self.top_front_left, 2, 1)

        self.top_front_right = QProgressBar()
        self.top_front_right.setMaximumHeight(20)
        self.top_front_right.setValue(0)
        self.thrusters_layout.addWidget(QLabel("FR"), 3, 0)
        self.thrusters_layout.addWidget(self.top_front_right, 3, 1)

        self.top_back_left = QProgressBar()
        self.top_back_left.setMaximumHeight(20)
        self.top_back_left.setValue(0)
        self.thrusters_layout.addWidget(QLabel("BL"), 4, 0)
        self.thrusters_layout.addWidget(self.top_back_left, 4, 1)

        self.top_back_right = QProgressBar()
        self.top_back_right.setMaximumHeight(20)
        self.top_back_right.setValue(0)
        self.thrusters_layout.addWidget(QLabel("BR"), 5, 0)
        self.thrusters_layout.addWidget(self.top_back_right, 5, 1)

        self.bottom_front_left = QProgressBar()
        self.bottom_front_left.setMaximumHeight(20)
        self.bottom_front_left.setValue(0)
        self.thrusters_layout.addWidget(QLabel("FL"), 2, 2)
        self.thrusters_layout.addWidget(self.bottom_front_left, 2, 3)

        self.bottom_front_right = QProgressBar()
        self.bottom_front_right.setMaximumHeight(20)
        self.bottom_front_right.setValue(0)
        self.thrusters_layout.addWidget(QLabel("FR"), 3, 2)
        self.thrusters_layout.addWidget(self.bottom_front_right, 3, 3)

        self.bottom_back_left = QProgressBar()
        self.bottom_back_left.setMaximumHeight(20)
        self.bottom_back_left.setValue(0)
        self.thrusters_layout.addWidget(QLabel("BL"), 4, 2)
        self.thrusters_layout.addWidget(self.bottom_back_left, 4, 3)

        self.bottom_back_right = QProgressBar()
        self.bottom_back_right.setMaximumHeight(20)
        self.bottom_back_right.setValue(0)
        self.thrusters_layout.addWidget(QLabel("BR"), 5, 2)
        self.thrusters_layout.addWidget(self.bottom_back_right, 5, 3)

class DepthWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initDepth()

    def initDepth(self):
        self.depth_layout = QGridLayout(self)
        self.depth_layout.setSpacing(30)
        self.setMaximumSize(200, 400)
        self.setStyleSheet("background: transparent;")
        self.setLayout(self.depth_layout)

        self.depth_label = QLabel("Depth")
        self.depth_label.setAlignment(Qt.AlignCenter)
        self.depth_layout.addWidget(self.depth_label, 0, 0)
        self.depth_label.setMaximumHeight(20)

        self.depth = QLCDNumber()
        self.depth.setMaximumSize(80, 30)
        self.depth.setDigitCount(5)
        self.depth.display(0.0)
        self.depth_layout.addWidget(self.depth, 1, 0)

class VelocityWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initVelocity()

    def initVelocity(self):
        self.velocity_layout = QGridLayout(self)
        self.velocity_layout.setSpacing(30)
        self.setMaximumSize(200, 400)
        self.setStyleSheet("background: transparent;")
        self.setLayout(self.velocity_layout)

        self.velocity_label = QLabel("Velocity")
        self.velocity_label.setAlignment(Qt.AlignCenter)
        self.velocity_layout.addWidget(self.velocity_label, 0, 0, 1, 2)
        self.velocity_label.setMaximumHeight(20)

        self.x = QLCDNumber()
        self.x.setMaximumSize(100, 100)
        self.x.setDigitCount(5)
        self.x.display(0.0)
        self.velocity_layout.addWidget(QLabel("X"), 1, 0)
        self.velocity_layout.addWidget(self.x, 1, 1)

        self.y = QLCDNumber()
        self.y.setMaximumSize(100, 100)
        self.y.setDigitCount(5)
        self.y.display(0.0)
        self.velocity_layout.addWidget(QLabel("Y"), 2, 0)
        self.velocity_layout.addWidget(self.y, 2, 1)

        self.z = QLCDNumber()
        self.z.setMaximumSize(100, 100)
        self.z.setDigitCount(5)
        self.z.display(0.0)
        self.velocity_layout.addWidget(QLabel("Z"), 3, 0)
        self.velocity_layout.addWidget(self.z, 3, 1)

class FineModeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initFineMode()

    def initFineMode(self):
        self.fine_layout = QGridLayout(self)
        self.fine_layout.setSpacing(30)
        self.setMaximumSize(200, 400)
        self.setStyleSheet("background: transparent;")
        self.setLayout(self.fine_layout)

        self.fine_label = QLabel("Fine Mode")
        self.fine_label.setAlignment(Qt.AlignCenter)
        self.fine_layout.addWidget(self.fine_label, 0, 0)
        self.fine_label.setMaximumHeight(20)

        self.fine = QLCDNumber()
        self.fine.setMaximumSize(75, 100)
        self.fine.setDigitCount(5)
        self.fine.display(0.0)
        self.fine_layout.addWidget(self.fine, 1, 0)
