#https://leetcode.com/problems/implement-queue-using-stacks/
#232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        val = self.peek()
        self.stack_2.pop()
        return val

    def peek(self) -> int:
        if self.empty():
            raise Exception('Queue Is Empty')
        if not self.stack_2:
            self._dump_stacks()
        return self.stack_2[-1]

    def empty(self) -> bool:
        return not self.stack_1 and not self.stack_2
    
    def _dump_stacks(self):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()