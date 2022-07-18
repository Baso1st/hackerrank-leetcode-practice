#https://leetcode.com/problems/invert-binary-tree/
#226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursive_invert(root)
        return root
        
    def recursive_invert(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.recursive_invert(node.left)
        self.recursive_invert(node.right)