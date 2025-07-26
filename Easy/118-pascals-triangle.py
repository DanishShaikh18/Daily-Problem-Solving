"""
Leetcode Problem #118  
Difficulty: Easy  
Link: https://leetcode.com/problems/pascals-triangle/
"""
from typing import List

class Solution:

    def generate_row(self, row):
        ans = 1
        ans_row = [1]

        for col in range(1, row):
            ans *= (row - col)
            ans //= col
            ans_row.append(ans)

        return ans_row

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            temp = self.generate_row(i)
            ans.append(temp)
        return ans

# Summary:
# 1. For each row, use combinatorial logic to compute binomial coefficients.
# 2. generate_row uses nCr = n! / (r!(n-r)!) optimized to avoid full factorials.
# 3. Append each generated row to the result list up to numRows.
