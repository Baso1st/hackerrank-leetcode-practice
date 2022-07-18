#https://leetcode.com/problems/balanced-binary-tree/
#110. Balanced Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_balance(root) >= 0

    def check_balance(self, node):
        if not node:
            return 0
        left_height = self.check_balance(node.left)
        right_height = self.check_balance(node.right)
        if abs(left_height - right_height) > 1:
            return float('-inf')
        else:
            return max(left_height, right_height) + 1