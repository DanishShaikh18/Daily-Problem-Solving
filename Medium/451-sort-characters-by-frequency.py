"""
Leetcode Problem #451  
Difficulty: Medium  
Link: https://leetcode.com/problems/sort-characters-by-frequency/
"""
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res = ''.join(char * freq for char, freq in c.most_common())
        return res

# Summary:
# 1. Count the frequency of each character using Counter.
# 2. Sort characters by frequency in descending order using most_common().
# 3. Build the result string by repeating each character 'freq' times.
