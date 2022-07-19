#https://leetcode.com/problems/majority-element/
#169. Majority Element


from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_table = defaultdict(int)
        n = len(nums)
        
        for num in nums:
            freq_table[num] += 1
            if freq_table[num] > (n // 2):
                return num

        
################### One hell of a good solution. Boyer-Moore Voting Algorithm ################

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count += 1
            else:
                count -= 1
            
        return candidate