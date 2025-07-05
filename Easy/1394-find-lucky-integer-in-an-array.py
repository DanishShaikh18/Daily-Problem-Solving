"""
Leetcode Problem #1394  
Difficulty: Easy  
Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/
"""
from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        lucky_numbers = [-1]

        for key in c:
            if key == c[key]:
                lucky_numbers.append(c[key])
        return max(lucky_numbers)
