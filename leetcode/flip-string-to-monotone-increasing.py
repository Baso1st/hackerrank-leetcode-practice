#https://leetcode.com/problems/flip-string-to-monotone-increasing/
#926. Flip String to Monotone Increasing
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = []
        zeroes = len([x for x in s[1:] if x == '0'])
        dp.append((0, zeroes))
        for i in range(1, n):
            ones, zeroes = dp[-1]
            if s[i-1] == '1':
                ones = dp[-1][0] + 1
            if s[i] == '0':
                zeroes = dp[-1][1] - 1
            dp.append((ones, zeroes))
            
        min_val = sum(dp[0])
        for pair in dp[1:]:
            sum_val = sum(pair)
            if sum_val < min_val:
                min_val = sum_val
        
        return min_val
            