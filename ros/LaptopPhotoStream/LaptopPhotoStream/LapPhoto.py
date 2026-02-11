import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class PhotoPublisher(Node):
    def __init__(self):
        super().__init__('photo_publisher')
        self.publisher_ = self.create_publisher(Image, '/photo/image', 10)
        self.bridge = CvBridge()

        self.timer = self.create_timer(1.0, self.publish_photo)
        self.image_path = os.path.expanduser("~/photo.jpg")

        self.get_logger().info("Photo publisher started")

    def publish_photo(self):
        if not os.path.exists(self.image_path):
            self.get_logger().warn("photo.jpg not found")
            return

        img = cv2.imread(self.image_path)
        msg = self.bridge.cv2_to_imgmsg(img, encoding='bgr8')
        msg.header.stamp = self.get_clock().now().to_msg()

        self.publisher_.publish(msg)
        self.get_logger().info("Photo sent")

def main():
    rclpy.init()
    node = PhotoPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
