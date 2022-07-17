#https://leetcode.com/problems/valid-parentheses/
#20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'{':'}', '(':')', '[':']'}
        stack = []
        
        for c in s:
            if c in lookup:
                stack.append(c)
            elif stack and c == lookup[stack[-1]]:
                stack.pop()
            else:
                return False
            
        return not stack
                
                