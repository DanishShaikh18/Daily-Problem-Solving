"""
Leetcode Problem #3  
Difficulty: Medium  
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

# Summary:
# 1. Use a sliding window (left, right pointers) to track the current substring.
# 2. Use a set `seen` to store unique characters.
# 3. If a duplicate is found, shrink the window from the left until valid.
# 4. Continuously update max_len as the longest valid substring seen so far.
