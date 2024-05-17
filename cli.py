import argparse
#from publisher import TurtleController

parser = argparse.ArgumentParser(description='Controlador')

parser.add_argument('--vx', type=float)

parser.add_argument('--vy', type=float)

parser.add_argument('--vtheta', type=float)

parser.add_argument('--t', type=float)

args = parser.parse_args()


print(args.vx, args.vy, args.vtheta, args.t)