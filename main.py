# This is the main to run and simulate robot vacuum cleans a room
from classes import *
import visualization

# How many Standard robot vacuum you want to use
num_standard_robots = 6
# How many Random-walk robot vacuum you want to use
num_random_robots = 2
# Enter the size of the room to be cleaned
width = 15
height = 15

if __name__ == "__main__":
  # Generate a room using width and height
  room = RectangularRoom(width, height)
  # Generate all robots
  robots = [] 
  for i in range(num_standard_robots):
    robots.append(StandardRobot(room, .3))
  for i in range(num_random_robots):
    robots.append(RandomWalkRobot(room, .6))
  # Total robots
  num_robots = num_standard_robots + num_random_robots
  
  # Create animation to plot the simulation
  animation = visualization.RobotVisualization(num_robots, width, height, 0.1)
  animation.update(room, robots)
  while room.getNumCleanedTiles() != room.getNumTiles():
    # Robot moves and cleans the room
    for robot in robots:
      robot.updatePositionAndClean()
    # Draw robot movement
    animation.update(room, robots)
  animation.done()
