import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

from mypkg.utils import get_wifi_signal


class WifiSignalPublisher(Node):
    def __init__(self):
        super().__init__('wifi_signal_publisher')

        self.publisher_ = self.create_publisher(Int32, 'wifi_signal', 10)
        self.timer = self.create_timer(1.0, self.publish_signal)

        self.get_logger().info("Wi-Fi Signal Publisher started")

    def publish_signal(self):
        rssi = get_wifi_signal()
        msg = Int32()
        msg.data = rssi

        self.publisher_.publish(msg)
        self.get_logger().info(f"Published Wi-Fi signal: {rssi} dBm")


def main(args=None):
    rclpy.init(args=args)
    node = WifiSignalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

