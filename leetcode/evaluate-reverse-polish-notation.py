#https://leetcode.com/problems/evaluate-reverse-polish-notation/
#150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if not t.strip('-').isnumeric():
                val2 = stack.pop()
                val1 = stack.pop()
                # result = int(eval(f"{val1}{t}{val2}"))
                result = self.do_math(val1, val2, t)
                stack.append(str(result))
            else:
                stack.append(t)
                
        return stack[0]

    
    def do_math(self, val1, val2, op):
        if op == '-':
            return int(val1) - int(val2)
        elif op == '+':
            return int(val1) + int(val2)
        elif op == '*':
            return int(val1) * int(val2)
        else:
            return int(int(val1) / int(val2))