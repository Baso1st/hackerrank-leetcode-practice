#https://leetcode.com/problems/largest-rectangle-in-histogram/
#84. Largest Rectangle in Histogram


############################ An average case is O(N LOG(N)). Worst case is O(N**2) when all the elements in the list are equal ########################################

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.recurse(heights, 0, len(heights))
    
    def recurse(self, heights, left, right):
        if left > right or left == len(heights):
            return -1
        if left == right:
            return heights[left]
        shortest = (0,float('inf'))
        for i, h in enumerate(heights[left:right]):
            if h < shortest[1]:
                shortest = (i+left, h)
                
        area1 = shortest[1] * (right - left)
        area2 = self.recurse(heights, left, shortest[0])
        area3 = self.recurse(heights, shortest[0]+1, right)
        return max(area1, area2, area3)
            
############################ A better time complexity solutions. It runs in O(N) ########################################

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = [-1]
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                top = stack.pop()
                area = heights[top] * (i - stack[-1] - 1)
                max_area = max(area, max_area)
            stack.append(i)
            
        while stack:
            top = stack.pop()
            if top != -1:
                area = heights[top] * (n - stack[-1] - 1)        
                max_area = max(area, max_area)
        
        return max_area
        