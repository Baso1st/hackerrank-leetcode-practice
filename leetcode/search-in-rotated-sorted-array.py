#https://leetcode.com/problems/search-in-rotated-sorted-array/
#33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        self.found = False
        self.idx = -1
        self.binary_search(0, len(nums))
        return self.idx
        
    def binary_search(self, i, j):
        if j <= i or self.found:
            return
        mid = (i + j) // 2
        if self.nums[mid] == self.target:
            self.found = True
            self.idx = mid
        
        self.binary_search(i, mid)
        self.binary_search(mid + 1, j)

################## A better solution from leetcode solution tab #######################
########## Here is the intution behind it 
# Formula: If a sorted array is shifted, if you take the middle, always one side will be sorted. Take the recursion according to that rule.

# 1- take the middle and compare with target, if matches return.
# 2- if middle is bigger than left side, it means left is sorted
# 2a- if [left] < target < [middle] then do recursion with left, middle - 1 (right)
# 2b- left side is sorted, but target not in here, search on right side middle + 1 (left), right
# 3- if middle is less than right side, it means right is sorted
# 3a- if [middle] < target < [right] then do recursion with middle + 1 (left), right
# 3b- right side is sorted, but target not in here, search on left side left, middle -1 (right)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1 