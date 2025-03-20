'''
https://leetcode.com/discuss/post/6524904/meta-l3-coding-problem-london-by-avatarg-fsuj/

You are running a gravity simulation involving falling boxes and exploding obstacles. The scenario is represented by a rectangular matrix of characters board.

Each cell of the matrix board contains one of three characters:

'-', which means that the cell is empty;
'*', which means that the cell contains an obstacle;
'#', which means that the cell contains a box.
The boxes all fall down simultaneously as far as possible, until they hit an obstacle, another grounded box, or the bottom of the board. If a box hits an obstacle, the box explodes, destroying itself and any other boxes within eight cells surrounding the obstacle. All the explosions happen simultaneously as well.

Given board, your task is to return the state of the board after all boxes have fallen.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(board[0].length · board.length2) will fit within the execution time limit.

For example:

board = [['#', '-', '#', '#', '*'],
         ['#', '-', '-', '#', '#'],
         ['-', '#', '-', '#', '-'],
         ['-', '-', '#', '-', '#'],
         ['#', '*', '-', '-', '-'],
         ['-', '-', '*', '#', '-']]

the output should be

solution(board) = [['-', '-', '-', '-', '*'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '*', '-', '-', '#'],
                   ['#', '-', '*', '-', '#']]

For example:

board = [['#', '#', '*'],
         ['#', '-', '*'],
         ['#', '-', '*'],
         ['-', '#', '#'],
         ['*', '-', '#'],
         ['*', '-', '-'],
         ['*', '-', '-']]

the output should be

solution(board) = [['-', '-', '*'],
                   ['-', '-', '*'],
                   ['-', '-', '*'],
                   ['-', '-', '-'],
                   ['*', '-', '-'],
                   ['*', '-', '#'],
                   ['*', '-', '#']]



constraints:
3 ≤ board.length ≤ 100,
3 ≤ board[i].length ≤ 100.
'''
