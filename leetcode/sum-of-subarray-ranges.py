#https://leetcode.com/problems/sum-of-subarray-ranges/
#2104. Sum of Subarray Ranges

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        total = 0
        
        for i in range(len(nums)):
            max_val, min_val = nums[i], nums[i]
            for j in range(i, len(nums)):
                max_val, min_val = self.get_max_min(max_val, min_val, nums[j])
                total += (max_val - min_val)
            
        return total
    
    
    def get_max_min(self, max_val, min_val, new_val):
        if new_val > max_val:
            return (new_val, min_val)
        elif new_val < min_val:
            return (max_val, new_val)
        else:
            return (max_val, min_val)