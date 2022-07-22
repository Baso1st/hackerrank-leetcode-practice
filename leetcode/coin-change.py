#https://leetcode.com/problems/coin-change/
#322. Coin Change


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float('inf')] * (amount + 1)
        cache[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if coin == i:
                    cache[i] = 1
                elif coin < i:
                    cache[i] = min(cache[i], cache[i-coin]+1)
               
        return cache[amount] if cache[amount] < float('inf') else -1
        
        