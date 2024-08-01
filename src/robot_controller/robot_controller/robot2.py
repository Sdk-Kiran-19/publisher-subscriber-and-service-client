import rclpy
from rclpy.node import Node
from custom_interface.msg import RobotMsg, ConfirmationMsg  # Ensure this matches your actual message definition

class Worker(Node):

    def __init__(self, robot_id):
        super().__init__('robot_worker')
        self.robot_id = robot_id
        self.subscription = self.create_subscription(
            RobotMsg,
            'robot_topic',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(ConfirmationMsg, 'confirmation_topic', 10)
        self.subscription  # Prevent unused variable warning

    def listener_callback(self, msg):
        if msg.id == self.robot_id:
            self.get_logger().info(f'Received message: id={msg.id}, load={msg.load}, unload={msg.unload}')
            # Process the message (e.g., perform tasks based on the message content)
            self.process_task(msg.id, msg.load, msg.unload)
        else:
            pass

    def process_task(self, robot_id, load, unload):
        # Implement your task processing logic here
        self.get_logger().info(f'Processing task for robot {robot_id} with load position {load} and unload position {unload}')
        # Simulate task completion
        self.get_logger().info(f'Task completed for robot {robot_id}')

        # Publish the confirmation message
        confirmation_msg = ConfirmationMsg()
        confirmation_msg.robot_id = robot_id
        confirmation_msg.success = True
        self.publisher_.publish(confirmation_msg)
        self.get_logger().info(f'Success confirmation sent for robot {robot_id}')

def main(args=None):
    rclpy.init(args=args)

    # Read the robot_id from the command line arguments
    robot_id = 2

    worker = Worker(robot_id)

    rclpy.spin(worker)

    worker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
