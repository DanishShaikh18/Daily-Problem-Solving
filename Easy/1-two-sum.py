"""
Leetcode Problem #1  
Difficulty: Easy  
Link: https://leetcode.com/problems/two-sum/
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # If no valid solution is found, return an empty list.
        return []

# Summary:
# 1. Use two nested loops to check all possible pairs of elements.
# 2. If a pair sums up to the target, return their indices.
# 3. Time complexity is O(n^2), which is acceptable for small inputs.
