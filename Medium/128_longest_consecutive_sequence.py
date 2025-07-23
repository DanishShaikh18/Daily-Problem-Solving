"""
Leetcode Problem #128  
Difficulty: Medium  
Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)        # Convert to set for O(1) lookup
        max_chain = 0              # To store the max sequence length

        for i in num_set:
            if i - 1 not in num_set:  # Check if it's the start of a sequence
                current = i
                chain = 1             # Initialize length for this sequence

                while current + 1 in num_set:  # Extend the sequence
                    current += 1
                    chain += 1

                max_chain = max(max_chain, chain)  # Track the longest found

        return max_chain  # Return the longest consecutive sequence length

# Summary:
# 1. Use a set to allow O(1) lookups.
# 2. For each number, only begin counting if it's the start of a sequence (i - 1 not in set).
# 3. Expand the sequence while next consecutive numbers exist.
# 4. Track and return the maximum length found.
