import rclpy#ROS 2のクライアントのためのライブラリ
from rclpy.node import Node#ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16#通信の型(16ビットの符号付き整数）

rclpy.init()
node = Node("listener")#ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Int16, "countup", 10)#パブリッシャのオブジェクト作成
n = 0#カウント用変数

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def  main():
    pub = node.create_subscription(Int16,"countup",cb,10)
    rclpy.spin(node)
