# https://leetcode.com/problems/two-sum-bsts/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        q = []
        q.append(root1)
        visited = []
        while q:
            front = q.pop(0)
            look_for = target - front.val
            if self.bst_find(root2, look_for):
                return True
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        
        return False
    
    def bst_find(self, node, val):
        if node:
            if node.val == val:
                return True
            elif val < node.val:
                return self.bst_find(node.left, val)
            elif val > node.val:
                return self.bst_find(node.right, val)
        return False