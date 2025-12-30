import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import pytest
import threading
import time

@pytest.fixture
def rclpy_init_shutdown():
    rclpy.init()
    yield
    rclpy.shutdown()

def test_wifi_alert_node(rclpy_init_shutdown):
    logs = []

    class TestAlertNode(Node):
        def __init__(self):
            super().__init__('test_alert_node')
            self.subscription = self.create_subscription(
                Int32,
                'wifi_signal',
                self.callback,
                10
            )

        def callback(self, msg):
            logs.append(msg.data)

    node = TestAlertNode()

    thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    thread.start()

    #alertノードを起動
    from mypkg.wifi_alert_node import WifiAlertNode
    alert_node = WifiAlertNode()

    alert_thread = threading.Thread(target=rclpy.spin, args=(alert_node,), daemon=True)
    alert_thread.start()

    #弱Wi-Fiをpublish
    pub = node.create_publisher(Int32, 'wifi_signal', 10)
    msg = Int32()
    msg.data = -90
    pub.publish(msg)

    time.sleep(1.0)

    assert -90 in logs

    node.destroy_node()
    alert_node.destroy_node()

