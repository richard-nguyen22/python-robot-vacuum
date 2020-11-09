from ps2_verify_movement27 import testRobotMovement
from classes import *

if __name__ == "__main__":
  # Call testRobotMovement to visualize how a StandardRobot clean a 5x5 room
  testRobotMovement(StandardRobot, RectangularRoom)
  # Call testRobotMovement to visualize how a RandomWalkRobot clean a 5x5 room
  testRobotMovement(RandomWalkRobot, RectangularRoom)