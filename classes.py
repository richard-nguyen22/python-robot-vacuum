import random
import math

class Position(object):
  """
  A Position represents a location in a two-dimensional room.
  """
  def __init__(self, x, y):
    """
    Initializes a position with coordinates (x, y).
    """
    self.x = x
    self.y = y
      
  def getX(self):
    return self.x
  
  def getY(self):
    return self.y
  
  def getNewPosition(self, angle, speed):
    """
    Computes and returns the new Position after a single clock-tick has
    passed, with this object as the current position, and with the
    specified angle and speed.

    Does NOT test whether the returned position fits inside the room.

    angle: number representing angle in degrees, 0 <= angle < 360
    speed: positive float representing speed

    Returns: a Position object representing the new position.
    """
    old_x, old_y = self.getX(), self.getY()
    angle = float(angle)
    # Compute the change in position
    delta_y = speed * math.cos(math.radians(angle))
    delta_x = speed * math.sin(math.radians(angle))
    # Add that to the existing position
    new_x = old_x + delta_x
    new_y = old_y + delta_y
    return Position(new_x, new_y)

  def __str__(self):  
      return "(%0.2f, %0.2f)" % (self.x, self.y)

class RectangularRoom(object):
  def __init__(self, width, height):
    """
    Initializes a rectangular room and all tiles with the specified width 
    and height. Initially, no tiles in the room have been cleaned.

    width: an integer > 0
    height: an integer > 0
    """
    self.width = width
    self.height = height
    self.hash_tiles = list() # Tiles
    for j in range(self.height):
      self.hash_tiles.append({})
      for i in range(self.width):
        self.hash_tiles[j][(i, j)] = ''
  
  def getNumTiles(self):
    """
    Return the total number of tiles in the room.

    returns: an integer
    """
    return self.width * self.height

  def cleanTileAtPosition(self, pos):
    """
    Mark the tile under the position POS as cleaned.

    Assumes that POS represents a valid position inside this room.

    pos: a Position
    """
    # Get current position
    pos_x = int(pos.getX())
    pos_y = int(pos.getY())
    # Update clean tile in self.hash_tiles
    self.hash_tiles[pos_y][(pos_x, pos_y)] = 'cleaned'
  
  def isTileCleaned(self, m, n):
    """
    Assumes that (m, n) represents a valid tile inside the room.

    m: an integer
    n: an integer

    returns: True if (m, n) tile is cleaned, False otherwise
    """
    return self.hash_tiles[n][(m,n)]  == 'cleaned'
  
  def getNumCleanedTiles(self):
    """
    Return the total number of clean tiles in the room.

    returns: an integer
    """
    cleaned_tiles = 0
    for pos_y in self.hash_tiles:
      for pos_tile in pos_y:
        if pos_y[pos_tile] == 'cleaned':
          cleaned_tiles += 1
    return cleaned_tiles

  def getRandomPosition(self):
    """
    Return a random position inside the room.

    returns: a Position object.
    """
    return Position(random.randrange(0, self.width),
                    random.randrange(0, self.height))

  def isPositionInRoom(self, pos):
    """
    pos: a Position object.
    returns: True if pos is in the room, False otherwise.
    """
    is_within_width = pos.getX() < self.width
    is_within_height = pos.getY() < self.height
    is_valid_pos = (pos.getX() >= 0 and pos.getY() >= 0)
    if is_within_width and is_within_height and is_valid_pos:
      return True
    else:
      return False


class Robot(object):
  """
  Represents a robot cleaning a particular room.

  At all times the robot has a particular position and direction in the room.
  The robot also has a fixed speed.

  Subclasses of Robot should provide movement strategies by implementing
  updatePositionAndClean(), which simulates a single time-step.
  """
  def __init__(self, room, speed):
    """
    Initializes a Robot with the given speed in the specified room. The
    robot initially has a random direction and a random position in the
    room. The robot cleans the tile it is on.
        
    room:  a RectangularRoom object.
    speed: a float (speed > 0)
    """
    self.room = room
    # Initialized position in the room
    self.pos = self.room.getRandomPosition()
    # Clean current tile
    self.room.cleanTileAtPosition(self.pos)     
    self.speed = speed
    # Initialize random direction
    self.direction = float(random.randrange(0, 360))

  def getRobotPosition(self):
    """
    Return the position of the robot.

    returns: a Position object giving the robot's position.
    """
    return self.pos
      
  def getRobotDirection(self):
    """
    Return the direction of the robot.

    returns: an integer d giving the direction of the robot as an angle in
    degrees, 0 <= d < 360.
    """
    return self.direction        

  def setRobotPosition(self, position):
    """
    Set the position of the robot to new `position`.

    position: a Position object.
    """        
    self.pos = position

  def setRobotDirection(self, direction):
    """
    Set the direction of the robot to DIRECTION.

    direction: integer representing an angle in degrees
    """
    self.direction = direction

  def updatePositionAndClean(self):
    """
    Simulate the raise passage of a single time-step.

    Move the robot to a new position and mark the tile it is on as having
    been cleaned.
    """
    # Update new position
    self.pos.getNewPosition(self.direction, self.speed)
    if self.room.isPositionInRoom(self.pos):
      # Move the robot to new position
      self.setRobotPosition(self.pos)
      # Clean the tile at new position
      self.room.cleanTileAtPosition(self.pos)
    else:
        print 'Opps! Robot may move out the room'        


class StandardRobot(Robot):
  """
  A StandardRobot is a Robot with the standard movement strategy

  At each time-step, a StandardRobot attempts to move in its current
  direction; when it would hit a wall, it *instead* chooses a new direction
  randomly.
  """
  def updatePositionAndClean(self):
    """
    Simulate the raise passage of a single time-step.

    Move the robot to a new position and mark the tile it is on as having
    been cleaned.
    """
    new_pos = self.pos.getNewPosition(self.direction, self.speed)
    # isPositionInRoom method to check if new position is in the room,
    # If not generate new direction and calculate new position in while loop
    # until the new position is in the room
    while (self.room.isPositionInRoom(new_pos) == False):
      # Generate another direction:
      self.setRobotDirection(random.randrange(0, 360))
      new_pos = self.pos.getNewPosition(self.direction, self.speed)        
    self.setRobotPosition(new_pos)
    if self.room.isTileCleaned(int(self.pos.getX()), int(self.pos.getY())):
      pass
    else:
      self.room.cleanTileAtPosition(self.pos)

  # Implement __str__ to print basic information of standard robot
  def __str__(self):
    return 'This is a standard robot which will change direction if it hits the wall'


class RandomWalkRobot(Robot):
  """
  A RandomWalkRobot is a robot with the "random walk" movement strategy: it
  chooses a new direction at random at the end of each time-step.
  """
  def updatePositionAndClean(self):
    """
    Simulate the passage of a single time-step.

    Move the robot to a new position and mark the tile it is on as having
    been cleaned.
    """
    new_pos = self.pos.getNewPosition(self.direction, self.speed)
    # isPositionInRoom method to check if new position is in the room,
    # If not generate new direction and calculate new position in while loop
    # until the new position is in the room
    while (self.room.isPositionInRoom(new_pos) == False):
      self.setRobotDirection(random.randrange(0, 360))
      new_pos = self.pos.getNewPosition(self.direction, self.speed)        
    # Update robot's new position
    self.setRobotPosition(new_pos)
    # Change robot's direction after each step
    self.setRobotDirection(random.randrange(0, 360))
    pos_x = int(self.pos.getX())
    pos_y = int(self.pos.getY())
    if (self.room.isTileCleaned(pos_x, pos_y) == False):
      self.room.cleanTileAtPosition(self.pos)
      
  # Implement __str__ to print basic information of random-walk robot
  def __str__(self):
    return 'This is a random-walk robot which will change direction after every step'
