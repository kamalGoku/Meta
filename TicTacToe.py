'''
348. Design Tic-Tac-Toe
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:

Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
'''

class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rowSum = [0 for _ in range(n)]
        self.colSum = [0 for _ in range(n)]
        self.diagonal = 0
        self.antiDiagonal = 0
        self.board = [[0 for _ in range(n)] for _ in range(n)]
    
    def move(self, row, col, player):
        if player==1:
            score = 1
        else:
            score = -1

        self.rowSum[row]+=score
        self.colSum[col]+=score
        if row==col:
            self.diagonal += score
        
        if col==self.n-row-1:
            self.antiDiagonal += score
        
        if self.isWin(row, col, player):
            print("Player ", player , " won")

        if abs(self.rowSum[row])==self.n or \
           abs(self.colSum[col])==self.n or \
           abs(self.diagonal)==self.n or \
           abs(self.antiDiagonal)==self.n:
            return player
        return 0

    def isWin(self, row, col, player):
        self.board[row][col] = player
        rows = 0
        cols = 0
        diagonal = 0
        antiDiagonal = 0
        for i in range(self.n):
            if self.board[row][i]==player:
                rows+=1
            if self.board[i][col]==player:
                cols+=1
            if self.board[i][i]==player:
                diagonal+=1
            if self.board[i][self.n-1-i]==player:
                antiDiagonal+=1
        if rows==self.n or cols==self.n or \
           diagonal==self.n or antiDiagonal==self.n:
            return True
        return False

g = TicTacToe(3)
print("Player 1 move (0,0) : ", g.move(0, 0, 1))
print("Player 2 move (1,1) : ", g.move(1, 1, 1))
print("Player 1 move (0,1) : ", g.move(0, 1, 1))
print("Player 2 move (0,0) : ", g.move(2, 2, 2))
print("Player 1 move (0,2) : ", g.move(0, 2, 1))
