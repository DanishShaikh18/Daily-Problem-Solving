"""
Leetcode Problem #75  
Difficulty: Medium  
Link: https://leetcode.com/problems/sort-colors/
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums.sort()

# Summary:
# 1. Sorts the array in-place using Python’s built-in `sort()`.
# 2. Though simple, it doesn't use the Dutch National Flag algorithm (optimal for this).
# 3. Acceptable for quick implementation, but not the most efficient for interview settings.
