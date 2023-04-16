# Determine if a 9 x9 Sudoku is valid. Only the filled cell 
# need to be validated "according to the following rules": 
# 1. Each row must contain the digits 1 - 9 without repitition. 
# 2. Each column must contain digits 1 - 9 without repitition. 
# 3. Each of the nine 3 x 3 sub-boxed of grid must contain the digits 1- 9 without repitition

# NOTES:
# - A sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.


import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[list[str]]) -> bool:
        
        # Three dictionaries are created to keep track of the used numbers in columns, rows, and 3x3 squares. 
        # Each dictionary stores the set of numbers used in the corresponding section of the board.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r /3, c /3)
        
        # Loop through each element of the board (9x9) and check if it's a valid number. If it's ".", skip to the next element.
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                # Check if the number already exists in the same row, column or 3x3 square. 
                # If it does, the board is invalid, return False.
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Add the number to the corresponding set for the row, column, and 3x3 square.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        # If the loop completed successfully, the board is valid, return True.
        return True

