"""
Leetcode Problem #1823  
Difficulty: Medium  
Link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
"""
from typing import List

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle: List[int] = [num for num in range(1, n + 1)]
        cur_ind: int = 0

        while len(circle) != 1:
            next_to_remove: int = (cur_ind + k - 1) % len(circle)
            circle.pop(next_to_remove)
            cur_ind = next_to_remove

        return circle[0]

# Summary:
# 1. Create a list of players numbered 1 to n.
# 2. Repeatedly remove every k-th person in the circle using modular indexing.
# 3. Continue until one person remains and return that winner.
