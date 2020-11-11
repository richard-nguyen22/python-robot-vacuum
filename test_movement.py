# Run to test robot movement
from classes import *
import visualization

# Room size
width = 3
height = 3

if __name__ == "__main__":
  # Generate a room with size 5x5
  room = RectangularRoom(width, height)
  # Generate a Standard robot
  standard_robot = StandardRobot(room, .3)
  # Visualize Standard robot movement
  animation = visualization.RobotVisualization(1, width, height, 0.1)
  animation.update(room, [standard_robot])
  while room.getNumCleanedTiles() != room.getNumTiles():
    # Robot moves and cleans the room
    standard_robot.updatePositionAndClean()
    # Draw robot movement
    animation.update(room, [standard_robot])
  animation.done()
  
  # Generate a Standard robot
  room = RectangularRoom(width, height)
  random_walk_robot = RandomWalkRobot(room, 1)
  # Visualize Random-walk robot movement
  animation = visualization.RobotVisualization(1, width, height, 0.4)
  animation.update(room, [random_walk_robot])
  while room.getNumCleanedTiles() != room.getNumTiles():
    # Robot moves and cleans the room
    random_walk_robot.updatePositionAndClean()
    # Draw robot movement
    animation.update(room, [random_walk_robot])
  animation.done()
