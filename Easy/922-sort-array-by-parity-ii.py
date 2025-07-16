"""
Leetcode Problem #922  
Difficulty: Easy  
Link: https://leetcode.com/problems/sort-array-by-parity-ii/
"""
from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 != 0]

        ans = []

        for i, j in zip(even, odd):
            ans.append(i)
            ans.append(j)
        return ans

# Summary:
# 1. Separate even and odd numbers into two lists.
# 2. Interleave them using zip to satisfy the parity condition (even at even index, odd at odd).
# 3. Return the combined list.
