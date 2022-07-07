#https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/
#1628. Design an Expression Tree With Evaluate Function


import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def evaluate(self):
        return int(self._post_order(self))
        

    def _post_order(self, node):
        if not node:
            return
        
        left = self._post_order(node.left)
        right = self._post_order(node.right)
        
        if node.val.isnumeric():
            return node.val
        else:
            return eval(f"{left}{node.val}{right}")
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        ops = set([x for x in postfix if not x.isnumeric()])
        for val in postfix:
            node = TreeNode(val)
            stack.append(node)
            if val in ops:
                op = stack.pop()
                right = stack.pop()
                left = stack.pop()
                op.right = right
                op.left = left
                stack.append(op)
                
        if len(stack) > 1:
            raise Exception('There should be only one node left in the stack')

        return stack.pop()
                
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        