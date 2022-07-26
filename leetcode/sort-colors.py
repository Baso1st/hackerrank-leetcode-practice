#https://leetcode.com/problems/sort-colors/
#75. Sort Colors

############## Quick Sort ###############

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums)-1)
        

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        
        p = self.partition(nums, left, right)
        
        if left < p -1:
            self.quick_sort(nums, left, p-1)
        
        if p < right:
            self.quick_sort(nums, p, right)
        
    
    def partition(self, nums, left, right):
        piviot = nums[(left + right) // 2]
        
        while left <= right:
            while nums[left] < piviot:
                left += 1
                
            while nums[right] > piviot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return left


################################## A better solution from leetcode solutions tab. time: O(N). Space: O(1) using one pass. Dutch National Flag Problem ######################


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = current = 0
        right = len(nums) - 1
        
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            else:
                current += 1