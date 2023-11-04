#!/usr/bin/env python
import cv2
import gi
import numpy as np
import command as command
gi.require_version('Gst', '1.0')
from gi.repository import Gst

class Video():

    def __init__(self):
        Gst.init(None)
        self.latest_frame = self._new_frame = None
        self.command = 'udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink emit-signals=true sync=false max-buffers=2 drop=true'
        self.video_pipe = None
        self.video_sink = None
        self.run(self.command)

    def start_gst(self, command):
        self.video_pipe = Gst.parse_launch(command)
        self.video_pipe.set_state(Gst.State.PLAYING)
        self.video_sink = self.video_pipe.get_by_name('appsink0')

    @staticmethod
    def gst_to_opencv(sample):
        buf = sample.get_buffer()
        caps_structure = sample.get_caps().get_structure(0)
        array = np.ndarray(
            (
                caps_structure.get_value('height'),
                caps_structure.get_value('width'),
                3
            ),
            buffer=buf.extract_dup(0, buf.get_size()), dtype=np.uint8)
        return array

    def frame(self):
        if self.frame_available:
            self.latest_frame = self._new_frame
            self._new_frame = None
        return self.latest_frame

    def frame_available(self):
        return self._new_frame is not None

    def run(self, command):
        self.start_gst(command)
        self.video_sink.connect('new-sample', self.callback)

    def callback(self, sink):
        sample = sink.emit('pull-sample')
        self._new_frame = self.gst_to_opencv(sample)
        return Gst.FlowReturn.OK

if __name__ == '__main__':
    video = Video()
    while not video.frame_available():
        cv2.waitKey(30)
    while True:
        if video.frame_available():
            frame = video.frame()
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
