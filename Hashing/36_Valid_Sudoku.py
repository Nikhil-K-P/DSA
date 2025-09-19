"""
36: Valid Sudoku
Level: Medium
Topics: Array, Hash Table, Matrix 
Link: https://leetcode.com/problems/valid-sudoku
Time Complexity: O(n^2), technically O(1) since n is constant (9 for a standard Sudoku)
Space Complexity: O(n)
"""


from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        m = len(board)
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)
        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] 
                    or board[r][c] in grids[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[(r//3, c//3)].add(board[r][c])
        return True 