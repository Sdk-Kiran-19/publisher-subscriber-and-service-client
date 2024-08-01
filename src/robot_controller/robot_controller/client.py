import rclpy 
from rclpy.node import Node
from custom_interface.srv import AddTwoInt
import sys

class Client(Node):
    def __init__(self):
        super().__init__('client_node')
        self.client = self.create_client(AddTwoInt,'add_num')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service")
        self.request = AddTwoInt.Request()


    def send_request(self,a,b):
        self.request.a = a
        self.request.b = b
        return self.client.call_async(self.request)
    
def main():
    rclpy.init()
    client = Client()
    future = client.send_request(int(sys.argv[1]),int(sys.argv[2]))
    rclpy.spin_until_future_complete(client,future)
    response = future.result()
    client.get_logger().info('Result of add_two_ints: %s + %s = %s ' %(sys.argv[1],sys.argv[2],response.sum))
    client.destroy_node()
    rclpy.shutdown()

if __name__=="__name__":
    main()
    