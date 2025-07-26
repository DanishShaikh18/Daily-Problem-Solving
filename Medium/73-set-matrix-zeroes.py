"""
Leetcode Problem #73  
Difficulty: Medium  
Link: https://leetcode.com/problems/set-matrix-zeroes/
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1  # Flag to track if the first column should be zero

        # 1st pass: mark rows and columns that need to be zeroed
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        # 2nd pass: set cells to 0 based on markers (excluding first row/col)
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        # Zero out first column if needed
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix

# Summary:
# 1. Use first row and first column as markers to avoid extra space.
# 2. If any cell is 0, mark its row and column by setting first cell of row/column to 0.
# 3. In second pass, set matrix[i][j] to 0 if its row or column is marked.
# 4. Handle first row and first column separately using flags.
