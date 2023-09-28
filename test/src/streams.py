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
import command as command

class CameraStreamWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.stream1_pipeline = "sudo gst-launch-1.0 udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        self.cap = cv2.VideoCapture(self.stream1_pipeline, cv2.CAP_GSTREAMER)

        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret:
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        self.cap.release()
        cv2.destroyAllWindows()

    #     self.video_label = QLabel(self)
    #     self.video_label.setAlignment(Qt.AlignCenter)

    #     layout = QGridLayout()
    #     layout.addWidget(self.video_label, 0, 0)
    #     self.setLayout(layout)

    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.update_frame)
    #     self.timer.start(30)  # Update frame every 30 milliseconds

    # def update_frame(self):
    #     ret, frame = self.video_capture.read()
    #     if ret:
    #         height, width, channel = frame.shape
    #         bytes_per_line = 3 * width
    #         q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
    #         pixmap = QPixmap.fromImage(q_image)
    #         self.video_label.setPixmap(pixmap)

    def launch_stream(self):

        # self.stream1_pipeline = "udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! appsink sync=false"
        # cap1 = cv.VideoCapture(self.stream1_pipeline, cv.CAP_GSTREAMER)

        # # self.stream2_pipeline = "udpsrc port=5601 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        # # cap2 = cv.VideoCapture(self.stream2_pipeline, cv.CAP_GSTREAMER)

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_frame)
        # self.timer.start(30)

        # put address from local machine into host command

        # gstreamer commands for starting stream on the pi
        launch_stream1 = "gst-launch-1.0 -v v4l2src device=/dev/video8 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.103 port=5600 sync=false buffer-size=1048576"
        launch_stream2 = "gst-launch-1.0 -v v4l2src device=/dev/video4 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.105 port=5601 sync=false buffer-size=1048576"
        launch_stream3 = "gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.104 port=5602 sync=false buffer-size=1048576"

        # starting subprocesses for each stream
        # subprocess.Popen(launch_stream1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        # subprocess.run(launch_stream2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        # subprocess.run(launch_stream3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)

        # gstreamer pipeline for receiving stream 
        receive_stream1 = "gst-launch-1.0 udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        receive_stream2 = "gst-launch-1.0 udpsrc port=5601 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
        # receive_stream3 = "gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.101 port=5602 sync=false buffer-size=1048576"
        
        # starting subprocesses for each stream
        # self.stream1_process = subprocess.Popen(receive_stream1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.stream2_process = subprocess.Popen(receive_stream2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.stream3_process = subprocess.Popen(receive_stream3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
