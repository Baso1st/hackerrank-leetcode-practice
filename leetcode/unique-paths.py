#https://leetcode.com/problems/unique-paths/
#62. Unique Paths

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
                

############################## A math solution. Refer to LeetCode solutions tab for explanation ###########################

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = math.comb(m+n-2, m-1)
        return count