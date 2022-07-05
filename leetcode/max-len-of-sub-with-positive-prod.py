#https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
#1567. Maximum Length of Subarray With Positive Product


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        max_len = 0
        for i in range(n):
            if nums[i] == 0:
                max_len = self.get_max_part(nums[start:i], max_len)
                start = i + 1
        
        max_len = self.get_max_part(nums[start:], max_len)
        return max_len
                
    def get_max_part(self, part, max_len):
        neg_count = sum([1 for x in part if x < 0])
        if neg_count % 2 == 0:
            max_len = max(len(part), max_len)
        else:                
            for i in range(len(part)):
                if part[i] < 0:
                    max_len = max(len(part[i+1:]), max_len)
                    break
            for i in range(len(part)-1, -1, -1):
                if part[i] < 0:
                    max_len = max(len(part[:i]), max_len)
                    break 
                    
        return max_len