#https://leetcode.com/problems/asteroid-collision/
#735. Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0 
        while i < len(asteroids):
            val = asteroids[i]
            if stack and val < 0 < stack[-1]:
                if abs(stack[-1]) > abs(val):
                    i += 1
                elif abs(stack[-1]) < abs(val):
                    stack.pop()
                else:
                    stack.pop()
                    i += 1
            else:
                stack.append(val) 
                i += 1
            
        return stack
                
          
                    