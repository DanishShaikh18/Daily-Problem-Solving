"""
Leetcode Problem #643  
Difficulty: Easy  
Link: https://leetcode.com/problems/maximum-average-subarray-i/
"""
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        msum = sum(nums[:k])  # Initial window sum
        sol = msum

        # Sliding the window over the array
        for r in range(k, len(nums)):
            msum += nums[r] - nums[r - k]  # Update window sum
            sol = max(sol, msum)           # Track maximum sum seen

        return sol / k  # Return maximum average

# Summary:
# 1. Use fixed-size sliding window of size k.
# 2. Calculate initial sum and slide the window updating the sum in O(1) time.
# 3. Keep track of the maximum sum and return average.
