"""
Leetcode Problem #645  
Difficulty: Easy  
Link: https://leetcode.com/problems/set-mismatch/
"""
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        extra = 0
        for key, value in c.items():
            if value == 2:
                extra = key  # The repeated number

        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        missing = expected_sum - (actual_sum - extra)

        return [extra, missing]

# Summary:
# 1. Count frequencies using Counter to find the repeated number.
# 2. Use expected sum formula to find what the missing number should be.
# 3. The missing number is calculated using: missing = expected_sum - (actual_sum - repeated).
