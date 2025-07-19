"""
Leetcode Problem #1876  
Difficulty: Easy  
Link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
"""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 2):  # Only go till len(s) - 3
            if len(set(s[i:i+3])) == 3:
                result += 1
        return result
