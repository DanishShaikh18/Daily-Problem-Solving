"""
Leetcode Problem #594  
Difficulty: Easy  
Link: https://leetcode.com/problems/longest-harmonious-subsequence/
"""
class Solution:
    def findLHS(self, nums):
        nums.sort()
        j = 0
        maxLength = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxLength = max(maxLength, i - j + 1)
        return maxLength

# Summary:
# 1. Sort the array to group close numbers together.
# 2. Use two pointers (i and j) to find subarrays where max - min == 1.
# 3. Track and update the maximum length of such subarrays.
