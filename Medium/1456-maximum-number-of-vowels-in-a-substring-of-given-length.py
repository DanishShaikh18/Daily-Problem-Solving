"""
Leetcode Problem #1456  
Difficulty: Medium  
Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = max_count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)

        return max_count
