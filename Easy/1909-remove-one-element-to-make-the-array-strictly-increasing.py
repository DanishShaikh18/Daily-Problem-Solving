"""
Leetcode Problem #1909  
Difficulty: Easy  
Link: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
"""
from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        ct = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                ct += 1
                if i > 0 and nums[i - 1] >= nums[i + 1]:
                    if i + 2 < len(nums) and nums[i] >= nums[i + 2]:
                        return False
        return ct <= 1

# Summary:
# 1. Traverse the array and count how many times the sequence breaks (nums[i] ≥ nums[i+1]).
# 2. If a break is found, check if removing either nums[i] or nums[i+1] can fix the sequence.
# 3. Return True if at most one such removal is needed, otherwise False.
