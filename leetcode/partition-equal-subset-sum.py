#https://leetcode.com/problems/partition-equal-subset-sum/
#416. Partition Equal Subset Sum


############################ The LeetCode solution tab has a very nice video explanation for this problem #################

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2
        
        memo = {}
        
        return self.possible(nums, 0, half, memo)
        
    
    def possible(self, nums, idx, target, memo):
        if target == 0:
            return True
        
        if target < 0 or idx >= len(nums):
            return False

        if (idx, target) in memo:
            return memo[(idx, target)]
        
        result = self.possible(nums, idx+1, target - nums[idx], memo) or self.possible(nums, idx+1, target, memo)
        memo[(idx, target)] = result
        return result



############################# DP solution From LeetCode solution tab ################################


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2
        
        dp = [[False]*(half + 1) for x in range(len(nums)+1)]
        
        for val in dp:
            val[0] = True
            
        for i in range(n-1, -1, -1):
            for j in range(half+1):
                if j < nums[i]:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] or dp[i+1][j-nums[i]]
        
        return dp[0][half]