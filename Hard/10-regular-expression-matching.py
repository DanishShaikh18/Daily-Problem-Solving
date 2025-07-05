"""
Leetcode Problem #10  
Difficulty: Hard  
Link: https://leetcode.com/problems/regular-expression-matching/
"""
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p, s) is not None

# Summary:
# 1. Use Python's `re.fullmatch()` to check if the entire string matches the pattern.
# 2. Returns True if it matches completely, otherwise False.
# 3. Note: This bypasses manual DP implementation by using built-in regex matching.
