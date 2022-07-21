#https://leetcode.com/problems/3sum/
#15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.nums = nums
        result = set()
        for i, val in enumerate(nums):
            target = 0 - val
            pairs = self.two_sum(i+1, target)
            for pair in pairs:
                v1, v2 = pair
                result.add(tuple(sorted([val, v1, v2])))
            
        return result
            
    def two_sum(self, i, target):
        num_set = set()
        results = []
        for val in self.nums[i:]:
            look_for = target - val
            if look_for in num_set:
                results.append((val, look_for))
            else:
                num_set.add(val)
        return results

####################### You should prefer the below solution ulness you are instructed not to sort the array ###################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        nums.sort()
        self.nums = nums
        result = []
        for i, v1 in enumerate(nums):
            if i > 0 and nums[i-1] == v1:
                continue
            target = 0 - v1
            pairs = self.two_sum(i+1, target)
            for pair in pairs:
                v2, v3 = pair
                result.append([v1, v2, v3])
            
        return result
            
    def two_sum(self, i, target):
        left = i
        right = self.n - 1
        pairs = []
        while left < right:
            s = self.nums[left] + self.nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                pairs.append((self.nums[left], self.nums[right]))
                left += 1
                right -= 1
                while left < self.n and self.nums[left] == self.nums[left - 1]:
                    left += 1
        return pairs