#https://leetcode.com/problems/maximum-subarray/
#53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tally = float('-inf')
        largest_sum = float('-inf')
        for val in nums:
            tally = max(val, tally + val)
            largest_sum = max(tally, largest_sum)
            
        return largest_sum
