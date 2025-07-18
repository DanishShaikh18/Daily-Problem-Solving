"""
Leetcode Problem #2269  
Difficulty: Easy  
Link: https://leetcode.com/problems/find-the-k-beauty-of-a-number/
"""
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        st = str(num)
        count = 0

        for i in range(len(st) - k + 1):
            curr = st[i:i+k]
            if int(curr) != 0 and num % int(curr) == 0:
                count += 1

        return count

# Summary:
# 1. Convert the number to a string to extract all k-length substrings.
# 2. For each substring, convert it to an integer and check if it divides the original number.
# 3. Count and return how many such substrings (divisors) exist.
