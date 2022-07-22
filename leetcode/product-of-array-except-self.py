#https://leetcode.com/problems/product-of-array-except-self/
#238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        result[0] = 1
        right = [1] * n
        right[n-1] = 1
        
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

            
        right = 1            
        for i in range(n-1, -1, -1):
            result[i] = result[i] * right
            right = nums[i] * right
            
        return result