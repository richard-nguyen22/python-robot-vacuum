# Prerequisites
Python 2.7 with package:
- matplotlib, to install use this command: `py pip -m install matplotlib`
- [Python 2.7 download link](https://www.python.org/downloads/release/python-2718/)

# Simulation of robot vacuum
iRobot is a company that sells [vacuuming robots](https://www.irobot.com/). The vacuuming robot moves around the floor, cleaning the area it passes over.

In simulation of robot vacuum project, a simulation model is build to compare how much time robot vacuum will take to clean the floor of a room.

## Simulation details
**The room**: The room is rectangular with given width `w` and height `h`. Initially the entire floor is dirty.

**Tiles**: The room with size (w * h) will have (w * h) tiles need to be cleaned. Each tile is identify by it coordination: (0, 0), (0, 1), ..., (w-1, h-1).

**Robot motion rules**:
- The robot is placed randomly inside the room.
- The robot has a direction of motion.
- All robots move at the same speed constantly throughout the simulation.
- If the robot detects that it will hit the wall, it will change a new direction randomly.

**Terminate the simulation**: The simulation ends when a specified fraction of the tiles in the room have been cleaned.

## Two type of robot vacuum
**Standard Robot** vacuum:
- A standard robot vacuum moves and cleans the floor in a straight line.
- If it hits the wall, it will change direction randomly

**Standard Robot** vacuum:
- A random-walk robot vacuum changes direction after each moving step. So the random-walk robot is kind of a *drunk* robot with random movement.

## Programming concepts
This robot vacuum simulation program uses Python 2.7 and object-oriented concepts to build all necessary classes such as: Robot, Room, Tile and Position.

# How to run Simulation of robot vacuum
File structures:
```
├── image -- contain image in README.md
classes.py -- All Classes are implemented here
main.py -- Python file to run the simulation
ps2_verify_movement27.pyc -- Code to test robot movement
ps2_visualize.py -- Code to plot the simulation
README.md -- Documentation of this simulation project
```

Open and run `main.py` to start the simulation:
- The 1st graph shows a Standard Robot vacuums a 5x5 room. The robot stops moving when all tiles are cleaned. Close the graph.
- The 2nd graph shows a Random-walk Robot vacuums a 5x5 room. The robot stops moving when all tiles are cleaned. Close the graph.

Sample graph with explanation:
![Sample graph](/image/simulation.png)