import rclpy
from rclpy.node import Node
from custom_interface.msg import RobotMsg, ConfirmationMsg  # Ensure this matches your actual message definition

class Controller(Node):

    def __init__(self, robot_id, load, unload):
        super().__init__('robot_controller')
        self.publisher_ = self.create_publisher(RobotMsg, 'robot_topic', 10)  # Ensure topic name is appropriate
        self.subscription = self.create_subscription(
            ConfirmationMsg,
            'confirmation_topic',
            self.listener_callback,
            10)
        self.subscription  # Prevent unused variable warning
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.id = robot_id
        self.load = load
        self.unload = unload

    def timer_callback(self):
        msg = RobotMsg()
        msg.id = self.id
        msg.load = self.load
        msg.unload = self.unload
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.id} {msg.load} {msg.unload}"')

    def listener_callback(self, msg):
        if msg.robot_id == self.id and msg.success:
            self.get_logger().info(f'Successful confirmation received for robot {msg.robot_id}')
            self.timer.cancel()
            self.destroy_node()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)

    robot_id = int(input("Enter robot ID: "))
    load = int(input("Enter load value: "))
    unload = int(input("Enter unload value: "))

    controller = Controller(robot_id, load, unload)

    rclpy.spin(controller)

    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
