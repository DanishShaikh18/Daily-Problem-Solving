"""
Leetcode Problem #387  
Difficulty: Easy  
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)

        # Step 1: Count frequency
        for ch in s:
            freq[ch] += 1

        # Step 2: Find first char with freq = 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1

# Summary:
# 1. Count the frequency of each character using a dictionary.
# 2. Loop through the string again to find the first character with frequency 1.
# 3. Return its index, or -1 if no unique character exists.
