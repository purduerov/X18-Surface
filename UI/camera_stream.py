# This is the stream widget class containing the four streams from the ROV -- 
# three front facing cameras and one bottom facing camera. 
# if you have a Mac, you will need to use the install command 'brew install gstreamer'
# this will allow you to run gst-launch-1.0

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import subprocess
import cv2
import numpy as np
import command as command

class CameraStreamWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initStream()

    def initStream(self):

        # creating the stream widget
        self.stream = QLabel()
        stream_layout = QGridLayout(self.stream)
        self.setLayout(stream_layout)

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

        # launching the stream 
        self.launch_stream()

    def launch_stream(self):

        # put address from local machine into host command

        # gstreamer commands for starting stream on the pi
        launch_stream1 = "gst-launch-1.0 -v v4l2src device=/dev/video8 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.101 port=5600 sync=false buffer-size=1048576"
        launch_stream2 = "gst-launch-1.0 -v v4l2src device=/dev/video4 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.101 port=5601 sync=false buffer-size=1048576"
        launch_stream3 = "gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.101 port=5602 sync=false buffer-size=1048576"

        # starting subprocesses for each stream
        # subprocess.Popen(launch_stream1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        # subprocess.run(launch_stream2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        # subprocess.run(launch_stream3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)

        # gstreamer pipeline for receiving stream 
        receive_stream1 = "gst-launch-1.0 udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        receive_stream2 = "gst-launch-1.0 udpsrc port=5601 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        # receive_stream3 = "gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.101 port=5602 sync=false buffer-size=1048576"
        
        # starting subprocesses for each stream
        self.stream1_process = subprocess.Popen(receive_stream1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stream2_process = subprocess.Popen(receive_stream2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.stream3_process = subprocess.Popen(receive_stream3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
