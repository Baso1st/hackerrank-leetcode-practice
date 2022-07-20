#https://leetcode.com/problems/diameter-of-binary-tree/
#543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self, node):
        if not node:
            return 0
        
        left_length = self.dfs(node.left)
        right_length = self.dfs(node.right)
        
        self.diameter = max(self.diameter, left_length + right_length)
        
        
        return max(left_length, right_length) + 1