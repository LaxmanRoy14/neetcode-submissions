from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create hash maps holding sets to track seen elements
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # Key will be a tuple: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells represented by "."
                if val == ".":
                    continue
                
                # Check if the value has already appeared in the current row, column, or sub-box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                # Store the value in the respective row, col, and sub-box sets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
                
        return True