"""
Leetcode Problem #164  
Difficulty: Medium  
Link: https://leetcode.com/problems/maximum-gap/
"""
class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        maxDiff = 0
        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, nums[i] - nums[i - 1])
        return maxDiff

# Summary:
# 1. If there are fewer than 2 elements, return 0 (no gap possible).
# 2. Sort the array and compute the difference between each adjacent pair.
# 3. Track and return the maximum of those differences.
