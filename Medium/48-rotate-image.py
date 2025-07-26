"""
Leetcode Problem #48  
Difficulty: Medium  
Link: https://leetcode.com/problems/rotate-image/
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap rows with columns)
        for i in range(n):
            for j in range(i):  # only swap upper triangle
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row to achieve 90° clockwise rotation
        for i in range(n):
            matrix[i].reverse()

        return matrix

# Summary:
# 1. Transpose: matrix[i][j] becomes matrix[j][i]
# 2. Reverse each row: turns transposed matrix into rotated matrix
# Example:
# Before: [[1,2,3],       After Transpose: [[1,4,7],      After Reverse: [[7,4,1],
#          [4,5,6],                          [2,5,8],                        [8,5,2],
#          [7,8,9]]                          [3,6,9]]                        [9,6,3]]
