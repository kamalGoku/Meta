'''
Given a mouse with 2 APIs in a maze. Design an algorithm to find a cheese in the maze using only the 2 given APIs shown below.

class Mouse {

	/**
	* Moves to one of the directions (left, right, up, down) and returns false if you can't move and true if you can.
	*/
	public boolean move(Direction direction);

	/**
	* Returns true if there is a cheese in the current cell.
	*/
	public boolean hasCheese();

	/**
	* Should return true and leave the mouse at that location or false if we can't find cheese and return the mouse back to where it started.
	*/
	public boolean getCheese() {
		// your code goes here
	}
}
'''
'''
Mouse and Cheese
'''
class Mouse:
    def __init__(self):
        self.directions = [(-1,0), #up
                      (0,1), #right
                      (1,0), #down
                      (0,-1) #left
                     ]
        self.oppDirections = [(1,0), #down
                              (0,-1), #left
                              (-1,0), #up
                              (0,1), #right
                             ]
        self.visited = set()

    def move(self,direction):
        pass

    def hasCheese(self):
        pass

    def __dfs(self,row, col):
        if self.hasCheese():
            return True
        self.visited.add((row, col))
        for i in range(4):
            dir = (dir+1)%4
            newRow = row+self.directions[dir][0]
            newCol = col+self.directions[dir][1]
            if (row, col) in self.visited:
                continue
            if not self.move(self.directions[i]):
                self.move(self.oppDirections[i])
                continue

            if self.__dfs(newRow, newCol):
                return True

            self.move(self.oppDirections[i])
        return False
    def getCheese(self):
        self.__dfs(0,0)
