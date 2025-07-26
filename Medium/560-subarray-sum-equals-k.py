"""
Leetcode Problem #560  
Difficulty: Medium  
Link: https://leetcode.com/problems/subarray-sum-equals-k/
"""
from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:

        n = len(arr) # size of the given array.
        mpp = defaultdict(int)
        preSum = 0
        cnt = 0

        mpp[0] = 1 # Setting 0 in the map.
        for i in range(n):
            # add current element to prefix Sum:
            preSum += arr[i]

            # Calculate x-k:
            remove = preSum - k

            # Add the number of subarrays to be removed:
            cnt += mpp[remove]

            # Update the count of prefix sum
            # in the map.
            mpp[preSum] += 1

        return cnt

# Summary:
# 1. Use prefix sum to track cumulative sums of subarrays.
# 2. Use a hashmap to store frequency of prefix sums.
# 3. For each prefix sum, check if (current_sum - k) exists in the map.
# 4. If it does, increment count by how many times that value occurred.
# 5. Update map with current prefix sum.
