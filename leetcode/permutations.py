#https://leetcode.com/problems/permutations/
#46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        perms.append([nums[0]])
        for val in nums[1:]:
            new_perms = []
            for perm in perms:
                perm.append(val)
                for i in range(len(perm)):
                    perm[i], perm[-1] = perm[-1], perm[i]
                    new_perms.append(list(perm))
                    perm[i], perm[-1] = perm[-1], perm[i]
            perms = new_perms
            
        return perms


######################### Leetcode backtracking solution #####################


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, 0, result)
        return result
    
    def backtrack(self, nums, first, result):
        n = len(nums)
        if first == n:
            result.append(list(nums))
            
        for i in range(first, n):
            nums[i], nums[first] = nums[first], nums[i]
            self.backtrack(nums, first + 1, result)
            nums[i], nums[first] = nums[first], nums[i]