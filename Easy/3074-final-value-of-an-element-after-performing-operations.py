"""
Leetcode Problem #3074  
Difficulty: Easy  
Link: https://leetcode.com/problems/final-value-of-an-element-after-performing-operations/
"""
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            # Find index of the first occurrence of the minimum value
            min_index = nums.index(min(nums))
            # Multiply that value by multiplier
            nums[min_index] *= multiplier
        return nums

# Summary:
# 1. For `k` times, find the first occurrence of the minimum value in the list.
# 2. Multiply that value by the given multiplier.
# 3. Return the modified list after all operations.
