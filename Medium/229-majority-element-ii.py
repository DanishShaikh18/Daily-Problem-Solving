"""
Leetcode Problem #229  
Difficulty: Medium  
Link: https://leetcode.com/problems/majority-element-ii/
"""
from collections import defaultdict
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate = Counter(nums)
        
        majority = len(nums) // 3

        ans = []

        for key, val in candidate.items():
            if val > majority:
                ans.append(key)

        return ans

# Summary:
# 1. Count frequencies of elements using Counter.
# 2. Any element appearing more than ⌊n/3⌋ times is a majority.
# 3. Iterate through the frequency map and collect all elements that satisfy the condition.
