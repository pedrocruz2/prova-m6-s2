import argparse
import rclpy
from geometry_msgs.msg import Twist
from publisher import TurtleController
parser = argparse.ArgumentParser(description='Controlador')

parser.add_argument('--vx', type=float)

parser.add_argument('--vy', type=float)

parser.add_argument('--vtheta', type=float)

parser.add_argument('--t', type=float)

args = parser.parse_args()

rclpy.init(args=None)
controller = TurtleController()
controller.add_to_deque(args.vx, args.vy, args.vtheta, args.t)
print(args.vx, args.vy, args.vtheta, args.t)