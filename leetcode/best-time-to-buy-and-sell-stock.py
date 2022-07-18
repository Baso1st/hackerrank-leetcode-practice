#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_profit = 0
        
        for val in prices:
            if val < min_val:
                min_val = val
                continue
            elif val - min_val > max_profit:
                max_profit = val - min_val
        
        return max_profit
            