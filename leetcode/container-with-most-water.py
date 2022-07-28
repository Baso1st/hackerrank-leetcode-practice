#https://leetcode.com/problems/container-with-most-water/
#11. Container With Most Water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = max_left = 0
        right = max_right = len(height) - 1
        going_left = False
        while left < right:
            if height[left] >= height[max_left] and height[right] >= height[max_right]: # This step to prune a little
                min_col = min(height[left], height[right])
                water = min_col * (right - left)
                max_water = max(max_water, water)
            if height[left] < height[right]:
                max_left = left
                left += 1
            else:
                max_right = right
                right -= 1
                
        return max_water