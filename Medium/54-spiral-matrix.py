"""
Leetcode Problem #54  
Difficulty: Medium  
Link: https://leetcode.com/problems/spiral-matrix/
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top = left = 0
        bottom = m - 1
        right = n - 1
        count = m * n
        ans = []

        while count > 0:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            count -= (right - left + 1)
            if top > bottom: break

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            count -= (bottom - top + 1)
            if count <= 0: break

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            count -= (right - left + 1)
            if count <= 0: break

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            count -= (bottom - top + 1)

        return ans

# Summary:
# 1. Uses 4 boundary pointers (top, bottom, left, right) to traverse matrix in spiral order.
# 2. Continues in 4 directions (→ ↓ ← ↑) while shrinking boundaries inward.
# 3. Stops when total elements collected equals m × n (count reaches 0).
