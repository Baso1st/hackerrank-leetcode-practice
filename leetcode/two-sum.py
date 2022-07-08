#https://leetcode.com/problems/two-sum/
#1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        
        for i, val in enumerate(nums):
            look_for = target - val
            if look_for in table:
                return [i, table[look_for]]
            
            table[val] = i

        raise Exception("Couldn't find an answer....")

        
        