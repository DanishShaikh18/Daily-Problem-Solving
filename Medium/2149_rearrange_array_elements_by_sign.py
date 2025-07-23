"""
Leetcode Problem #2149  
Difficulty: Medium  
Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1

        for i in nums:
            if i > 0:
                ans[pos] = i
                pos += 2
            else:
                ans[neg] = i
                neg += 2
        return ans

# Summary:
# 1. Create a new result array of same size.
# 2. Use two pointers: `pos` (even index) for positive nums, `neg` (odd index) for negative nums.
# 3. Loop through input; place positives at `pos`, negatives at `neg`.
# 4. Return rearranged array with alternating signs.
