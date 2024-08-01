import rclpy 
from rclpy.node import Node
from custom_interface.srv import AddTwoInt
import sys

class Service(Node):
    def __init__(self):
        super().__init__("Service_node")
        self.get_logger().info("Service node running")
        self.service = self.create_service(AddTwoInt,'add_num',self.add_callback)

    def add_callback(self,request,response):
        response.sum = request.a + request.b
        self.get_logger().info('Result of add_two_ints: %d ' %(int(response.sum)))
        return response
    
def main():
    rclpy.init()
    service = Service()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__=="__main__":
    main()
