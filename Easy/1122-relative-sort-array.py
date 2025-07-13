"""
Leetcode Problem #1122  
Difficulty: Easy  
Link: https://leetcode.com/problems/relative-sort-array/
"""
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1, arr2):
        count_map = defaultdict(int)
        remaining = []
        result = []

        # Initialize count map with relative order elements
        for num in arr2:
            count_map[num] = 0

        # Count occurrences of elements in target array
        for num in arr1:
            if num in count_map:
                count_map[num] += 1
            else:
                remaining.append(num)

        # Sort the remaining elements
        remaining.sort()

        # Add elements as per relative order
        for num in arr2:
            result.extend([num] * count_map[num])

        # Add remaining elements
        result.extend(remaining)

        return result

# Summary:
# 1. Count how often each arr2 element appears in arr1.
# 2. Store elements not in arr2 in a separate list and sort them.
# 3. Add elements in arr2's order using counts, then append the sorted leftovers.
