# Determine if a 9 x9 Sudoku is valid. Only the filled cell 
# need to be validated "according to the following rules": 
# 1. Each row must contain the digits 1 - 9 without repitition. 
# 2. Each column must contain digits 1 - 9 without repitition. 
# 3. Each of the nine 3 x 3 sub-boxed of grid must contain the digits 1- 9 without repitition

# NOTES:
# - A sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[list[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[r] or
                    board[r][c] in square[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
            return True
