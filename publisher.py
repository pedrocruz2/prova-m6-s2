from collections import deque
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time 

class TurtleController(Node): 
    def __init__(self):
        super().__init__('turtle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.deq = deque()
        time.sleep(2)

    def add_to_deque(self,vx,vy,vtheta,tempo):
        self.deq.append([vx,vy,vtheta,tempo])

    def move(self):
        deq = self.deq
        try:
            instructions = deq.pop()
            msg = Twist()
            msg.linear.x = instructions[0]
            msg.linear.y = instructions[1]
            msg.angular.z = instructions[2]
            self.publisher_.publish(msg)
            time.sleep(instructions[3])
            return self.move()
        except:
            time.sleep(2)
            msg = Twist()
            msg.linear.x = 0.0
            msg.linear.y = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            print('Deque Vazio')
        return self.move()
rclpy.init(args=None)
controller = TurtleController()
controller.move()




