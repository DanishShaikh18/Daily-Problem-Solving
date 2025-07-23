"""
Leetcode Problem #31  
Difficulty: Medium  
Link: https://leetcode.com/problems/next-permutation/
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # Step 2: If no such element found, the array is in descending order
        if ind == -1:
            nums.reverse()
            return

        # Step 3: Find the next greater element from the right and swap
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 4: Reverse the suffix after the swapped element
        nums[ind + 1:] = reversed(nums[ind + 1:])

# Summary:
# 1. Traverse from end to find first decreasing element (pivot).
# 2. If not found, array is the last permutation → reverse to get the first.
# 3. Find smallest number greater than pivot to the right, and swap.
# 4. Reverse the suffix to get the next lexicographically smallest permutation.
