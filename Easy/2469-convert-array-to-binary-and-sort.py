"""
Leetcode Problem #2469  
Difficulty: Easy  
Link: https://leetcode.com/problems/convert-array-to-binary-and-sort/
"""
from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        nums.sort()
        return nums

# Summary:
# 1. Convert each number in the array to 0 if even, 1 if odd.
# 2. Sort the resulting binary array in ascending order.
# 3. Return the transformed and sorted array.
