#https://leetcode.com/problems/min-stack/
#155. Min Stack

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MinStack:
    def __init__(self):
        self.arr = []
        self.head = None
        
    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.head:
            self.head = Node(val)
        elif val <= self.head.val:
            node = Node(val)
            node.next = self.head
            self.head = node
        

    def pop(self) -> None:
        top = self.arr.pop()
        if top == self.head.val:
            self.head = self.head.next
        return top

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.head.val
        
################################# A similar complexity solution, but more elegant and doesn't need a linkedlist#################
        
class MinStack:
    def __init__(self):
        self.arr = []
        
    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append((val, val))
        else:
            min_val = min(self.arr[-1][1], val)
            self.arr.append((val, min_val))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()