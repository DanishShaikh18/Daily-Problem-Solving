"""
Leetcode Problem #2099  
Difficulty: Easy  
Link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
"""
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair with indices
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value descending
        nums_with_indices.sort(key=lambda x: -x[0])
        
        # Take top k and sort by original index
        top_k = sorted(nums_with_indices[:k], key=lambda x: x[1])
        
        # Extract values
        return [num for num, _ in top_k]

# Summary:
# 1. Pair each number with its original index.
# 2. Sort by number in descending order and select top k values.
# 3. Sort those k elements back to their original order using indices.
# 4. Extract and return the values only.
