"""
Leetcode Problem #231  
Difficulty: Easy  
Link: https://leetcode.com/problems/power-of-two/
"""
from typing import Any

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))

# Summary:
# 1. Check if the number is positive (n > 0), since powers of two must be positive.
# 2. Use the bitwise trick: (n & (n - 1)) removes the lowest set bit.
# 3. If the result is zero, it indicates `n` had only one set bit—hence it’s a power of two.
