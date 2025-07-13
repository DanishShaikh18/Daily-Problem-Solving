"""
Leetcode Problem #1  
Difficulty: Easy  
Link: https://leetcode.com/problems/two-sum/
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Stores number → index

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[num] = i

