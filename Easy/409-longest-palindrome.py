"""
Leetcode Problem #409  
Difficulty: Easy  
Link: https://leetcode.com/problems/longest-palindrome/
"""
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charFrequency = Counter(s)
        oddFrequencyCount = 0
        for frequency in charFrequency.values():
            if frequency % 2 == 1:
                oddFrequencyCount += 1
        if oddFrequencyCount > 1:
            return len(s) - oddFrequencyCount + 1
        return len(s)

# Summary:
# 1. Count frequency of each character.
# 2. Characters with even frequency can fully contribute to a palindrome.
# 3. At most one character with odd frequency can sit in the center — subtract extra odd counts.
