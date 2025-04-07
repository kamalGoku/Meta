'''
Given a  robot cleaner in a room modeled as a grid.
Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right.
Each turn it made is 90 degrees.
When it tries to move into a blocked cell, its bumper sensor detects the 
obstacle and it stays on the current cell.
Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
'''

class Robot:
  #returns true if next cell is open and robot moves into the cell.
  #returns false if next cell is obstacle and robot stays on the current cell.
  def move(self):
    pass

  #Robot will stay on the same cell after calling turnLeft/turnRight.
  #Each turn will be 90 degrees.
  def turnLeft(self):
    pass
  def turnRight(self):
    pass

  #Clean the current cell.
  def clean(self):
    pass

directions = [(-1,0), #Up
              (0,1), #Right
              (1,0), #Down
              (0,-1) #Left
              ]

room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
]
row =1
col = 3

visited = set()

def goBack(robot):
    robot.turnRight()
    robot.turnRight()
    robot.move()
    robot.turnRight()
    robot.turnRight()

def dfs(robot, row, col, currDir):
  robot.clean()
  visited.add((row, col))
  for i in range(4):
    newDir = (currDir+i)%4
    newRow = row+directions[newDir][0]
    newCol = col+directions[newDir][1]
    if (newRow,newCol) not in visited and robot.move():
      dfs(robot, newRow, newCol, newDir)
      goBack(robot) #backtrack
    
    robot.turnRight() #move to next Dir
    
robot = Robot()
dfs(robot, row, col, 0)#row, col, dir
