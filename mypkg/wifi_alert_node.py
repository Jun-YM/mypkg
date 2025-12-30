import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class WifiAlertNode(Node):
    def __init__(self):
        super().__init__('wifi_alert_node')

        self.declare_parameter('threshold', -70)
        self.threshold = self.get_parameter('threshold').value

        self.subscription = self.create_subscription(
            Int32,
            'wifi_signal',
            self.signal_callback,
            10
        )

        self.alert_publisher = self.create_publisher(String, 'wifi_alert', 10)

        self.get_logger().info(
            f"Wi-Fi Alert Node started (threshold={self.threshold} dBm)"
        )

    def signal_callback(self, msg):
        rssi = msg.data

        if rssi < self.threshold:
            alert_msg = String()
            alert_msg.data = f"Warning: Wi-Fi signal is weak ({rssi} dBm)"
            self.alert_publisher.publish(alert_msg)
            self.get_logger().warn(alert_msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = WifiAlertNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

