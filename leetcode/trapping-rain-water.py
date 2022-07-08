#https://leetcode.com/problems/trapping-rain-water/
#42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        prev = (0, -1)
        stack = [prev] # (idx, val)
        for i, val in enumerate(height):
            current = (i, val)
            if val >= prev[1]:
                if stack[-1][0] + 1 == i: # adjacent idx
                    stack.pop()
                while stack and len(stack) > 1 and val >= stack[-1][1] < stack[-2][1]:
                    stack.pop()
                stack.append(current)
            prev = current
        
        stack.pop(0)
        prev = stack.pop(0)
        
        water = 0
        for idx, val in stack:
            start_idx = prev[0] + 1
            h = min(prev[1], val)
            w = idx - start_idx
            area = h * w
            dirt = sum([min(x, h) for x in height[start_idx:idx]])
            water += (area - dirt)
            prev = (idx, val)
        return water


################################# A simpler solution found in the solution tab of LeetCode #################################
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [None] * n
        right_max = [None] * n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        
        for i in range(1, n):
            val = height[i]
            left_max[i] = max(left_max[i-1], val)
        
        
        for i in range(len(height)-2, -1, -1):
            val = height[i]
            right_max[i] = max(right_max[i+1], val)
            
        water = 0
        for i, val in enumerate(height):
            water += min(left_max[i], right_max[i]) - val
            
        return water
        