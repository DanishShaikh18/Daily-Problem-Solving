"""
Leetcode Problem #1250  
Difficulty: Hard  
Link: https://leetcode.com/problems/check-if-it-is-a-good-array/
"""
from math import gcd

class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        return gcd(*nums) == 1

# Summary:
# 1. A "good array" means we can form 1 by some linear combination of elements.
# 2. Mathematically, this is true if the GCD of all elements is 1.
# 3. Use Python's unpacking with `gcd(*nums)` to check this directly.
