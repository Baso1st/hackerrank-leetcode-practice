#https://leetcode.com/problems/maximum-subarray-min-product/
#1856. Maximum Subarray Min-Product
# I couldn't come up with a solution that's bettern than O(n**2) So I found the following solution on leetcode discussion tab. It runs in O(N)

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums.append(0)
        stack = [(-1, 0)] # (min_val, running_sum)
        running_sum = max_min_prod = 0
        
        for val in nums:
            while val <= stack[-1][0]:
                min_val, _ = stack.pop()
                min_prod = min_val * (running_sum - stack[-1][1])
                max_min_prod = max(min_prod, max_min_prod)
            running_sum += val
            stack.append((val, running_sum))
            
        return max_min_prod % (10**9+7)
        
