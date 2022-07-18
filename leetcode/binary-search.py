#https://leetcode.com/problems/binary-search/
#704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums), target)
    
    def binary_search(self, nums, start, end, target):
        if end <= start:
            return -1
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binary_search(nums, start, mid, target)
        else:
            return self.binary_search(nums, mid+1, end, target)
        