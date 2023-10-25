from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import subprocess
import command as command

class CameraStreamWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initStream()

    def initStream(self):

        self.stream = QLabel()
        stream_layout = QGridLayout(self.stream)
        self.setLayout(stream_layout)

        self.launch_stream()

    def launch_stream(self):

        # gstreamer commands for starting stream on the pi
        launch_stream1 = "gst-launch-1.0 -v v4l2src device=/dev/video8 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.103 port=5600 sync=false buffer-size=1048576"
        launch_stream2 = "gst-launch-1.0 -v v4l2src device=/dev/video4 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.103 port=5601 sync=false buffer-size=1048576"
        # launch_stream3 = "gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.101 port=5602 sync=false buffer-size=1048576"

        # gstreamer pipeline for receiving stream 
        receive_stream1 = "gst-launch-1.0 udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        receive_stream2 = "gst-launch-1.0 udpsrc port=5601 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        # receive_stream3 = "gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.101 port=5602 sync=false buffer-size=1048576"
        
        self.stream1_process = subprocess.Popen(receive_stream1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.stream2_process = subprocess.Popen(receive_stream2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.stream3_process = subprocess.Popen(receive_stream3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)