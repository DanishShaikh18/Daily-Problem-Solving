"""
Leetcode Problem #912  
Difficulty: Medium  
Link: https://leetcode.com/problems/sort-an-array/
"""
from typing import List

class Solution:

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

# Summary:
# 1. Implements Merge Sort — a divide and conquer sorting algorithm.
# 2. Recursively splits the array into halves, sorts each, and merges them.
# 3. The merge step combines two sorted arrays into one.
