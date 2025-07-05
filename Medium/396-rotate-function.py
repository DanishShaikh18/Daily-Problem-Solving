"""
Leetcode Problem #396  
Difficulty: Medium  
Link: https://leetcode.com/problems/rotate-function/
"""
class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        
        max_val = F
        
        for i in range(1, n):
            F = F + total_sum - n * nums[-i]
            max_val = max(max_val, F)
        
        return max_val

# Summary:
# 1. Calculate F(0) as the base value.
# 2. Use the formula F(k) = F(k-1) + total_sum - n * nums[n - k] to avoid recomputing.
# 3. Track and return the maximum F(k) value found.
