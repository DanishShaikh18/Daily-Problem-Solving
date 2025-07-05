"""
Leetcode Problem #49  
Difficulty: Medium  
Link: https://leetcode.com/problems/group-anagrams/
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))  
            grouped[key].append(word)

        return list(grouped.values())

# Summary:
# 1. Sort each word to form a key — anagrams will have the same sorted key.
# 2. Group words by their sorted key using a defaultdict.
# 3. Return all grouped anagram lists.
