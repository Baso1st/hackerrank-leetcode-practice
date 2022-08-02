#https://leetcode.com/problems/basic-calculator/
#224. Basic Calculator

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for c in s:
            if c == ' ':
                continue
            if c == ')':
                sub = []
                while stack[-1] != '(':
                    sub.append(stack.pop())
                stack.pop()
                total = self.new_eval(''.join(reversed(sub)))
                if total[0] == '-' and stack:
                    if stack[-1] == '-':
                        stack.pop()
                        total = '+' + total[1:]
                    elif stack[-1] == '+':
                        stack.pop()
                stack.append(total)
            else:
                stack.append(c)              
        return self.new_eval(''.join(stack))
    
    
    def new_eval(self, s):
        if s[0] == '-':
            s = '0' + s
        ops = []
        curr = []
        for c in s:
            if c == '+' or c == '-':
                ops.append(''.join(curr))
                ops.append(c)
                curr = []
            else:
                curr.append(c)

        ops.append(''.join(curr))

        stack = []
        while ops:
            front = ops.pop(0)
            if front == '+':
                new_op = ops.pop(0)
                stack[-1] += int(new_op)
            elif front == '-':
                new_op = ops.pop(0)
                stack[-1] -= int(new_op)
            else:
                stack.append(int(front))
        
        return str(stack[0])
    
            
            
############################### LeetCode soluiont tab has a much smaller solution with a better performance #################################


class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        operand = 0
        res = 0
        stack = []
        for c in s:
            if c.isdigit():
                operand = (10 * operand) + int(c)
            elif c == '+':
                res += (sign * operand)
                sign = 1
                operand = 0
            elif c == '-':
                res += (sign * operand)
                sign = -1
                operand = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += (sign * operand)
                res *= stack.pop()
                res += stack.pop()
                operand = 0
            
        return res + (sign * operand)
            
            
            
        