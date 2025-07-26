"""
Leetcode Problem #18  
Difficulty: Medium  
Link: https://leetcode.com/problems/4sum/
"""
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        summ = 0
        ans = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                k = len(nums) - 1
                while l < k:
                    summ = nums[i] + nums[j] + nums[l] + nums[k]

                    if summ == target:
                        ans.append([nums[i], nums[j], nums[l], nums[k]])
                        l += 1
                        k -= 1
                        while l < k and nums[l] == nums[l - 1]:
                            l += 1
                        while k > l and nums[k] == nums[k + 1]:
                            k -= 1
                    elif summ < target:
                        l += 1
                    elif summ > target:
                        k -= 1
        return ans

# Summary:
# 1. Sort the array to simplify duplicate handling and enable two-pointer technique.
# 2. Use two nested loops to fix the first two elements.
# 3. Apply two-pointer strategy (l, k) to find remaining two numbers such that their sum equals target.
# 4. Skip duplicates at every level to avoid repeating quadruplets.
