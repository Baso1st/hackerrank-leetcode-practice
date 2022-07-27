#https://leetcode.com/problems/subsets/
#78. Subsets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        
        for val in nums:
            output += [curr + [val] for curr in output] 
    
        return output

########################### A better space complexity solution using backtracking found in LeetCode 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.output = []
        
        for size in range(self.n+1):
            self.backtrack(0, size, [])
        
        return self.output
    
    def backtrack(self, start: int, size: int, current: List[int]):
        if len(current) == size:
            self.output.append(list(current))
            return
            
        for i in range(start, self.n):
            current.append(self.nums[i])
            self.backtrack(i+1, size, current)
            current.pop()