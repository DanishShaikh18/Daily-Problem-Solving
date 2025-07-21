"""
Leetcode Problem #121  
Difficulty: Easy  
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = profit = 0 
        max_profit = float('-inf')

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]

            if profit > max_profit:
                max_profit = profit
            
            if prices[r] < prices[l]:
                l = r

        return 0 if max_profit < 0 else max_profit

# Summary:
# 1. Use two pointers: `l` for buying day, `r` for selling day.
# 2. If current price is lower than buying price, update `l`.
# 3. Track profit and update `max_profit` if current profit is higher.
# 4. Return 0 if no profit was possible; else return max profit found.
