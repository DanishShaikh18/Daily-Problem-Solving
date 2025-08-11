"""
Leetcode Problem #3477  
Difficulty: Easy  
Link: https://leetcode.com/problems/fruits-into-baskets-ii/
"""
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        alloted = 0
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    baskets[j] = -1  # mark this basket as used
                    alloted += 1
                    break
        return n - alloted

# Summary:
# 1. Iterate over each fruit and try to place it in the first available basket that can hold it.
# 2. If placed, mark the basket as used (-1) and increment the `alloted` count.
# 3. Return total fruits minus the placed fruits to get the number of unplaced fruits.
