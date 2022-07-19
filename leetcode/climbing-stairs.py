#https://leetcode.com/problems/climbing-stairs/
#70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        cache = [0] * (n + 1)
        cache[1] = 1
        cache[2] = 2
        
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]
    
    
######### A better solution, just like fibonacci ###############    

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        first = 1
        second = 2
        
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
            
        return second