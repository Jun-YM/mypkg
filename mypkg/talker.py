import rclpy
from rclpy.node import Node
from person_msgs.srv import Query
from person_msgs.msg import Person
rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0

def cb(request, response):
    if request.name == "上田隆一":
        response.age = 46
    else:
        response.age = 255

    return response


def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)
