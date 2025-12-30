import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import pytest
import time

@pytest.fixture
def rclpy_init_shutdown():
    rclpy.init()
    yield
    rclpy.shutdown()

def test_wifi_signal_publisher(rclpy_init_shutdown):
    received_messages = []

    class TestSubscriber(Node):
        def __init__(self):
            super().__init__('test_subscriber')
            self.subscription = self.create_subscription(
                Int32,
                'wifi_signal',
                self.callback,
                10
            )

        def callback(self, msg):
            received_messages.append(msg.data)

    node = TestSubscriber()

    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(node)

    from mypkg.wifi_signal_publisher import WifiSignalPublisher
    pub_node = WifiSignalPublisher()
    executor.add_node(pub_node)

    start = time.time()
    while time.time() - start < 2.0:
        executor.spin_once(timeout_sec=0.1)

    assert len(received_messages) > 0
    assert isinstance(received_messages[0], int)

    executor.shutdown()
    node.destroy_node()
    pub_node.destroy_node()

