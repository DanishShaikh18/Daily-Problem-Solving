"""
Leetcode Problem #15  
Difficulty: Medium  
Link: https://leetcode.com/problems/3sum/
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i = 0
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                elif summ < 0:
                    j += 1
                elif summ > 0:
                    k -= 1
        return ans

# Summary:
# 1. Sort the array to efficiently avoid duplicates and use two-pointer technique.
# 2. Fix one element and find two others such that their sum is zero.
# 3. Skip duplicate values to avoid repeating triplets in the result.
# 4. Use two-pointer approach for checking pairs that sum with the fixed element to zero.
# 5. Return all unique triplets that sum to zero.