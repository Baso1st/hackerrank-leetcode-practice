#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#230. Kth Smallest Element in a BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        for i, val in enumerate(self.pre_order(root)):
            if i+1 == k:
                return val
    
    def pre_order(self, node):
        if not node:
            return 
        
        yield from self.pre_order(node.left)
        yield node.val
        yield from self.pre_order(node.right)