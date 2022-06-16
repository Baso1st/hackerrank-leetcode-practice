#https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        possible_subs = []
        self.pre_order(root, subRoot.val, possible_subs)
        for node in possible_subs:
            q = []
            q.append(node)
            q_ref = []
            q_ref.append(subRoot)
            match = True
            while q and q_ref:
                front = q.pop(0)
                front_ref = q_ref.pop(0)
                if front_ref.val != front.val:
                    match = False
                    break
                
                if (front.left and not front_ref.left) or (front.right and not front_ref.right) \
                or (front_ref.left and not front.left) or (front_ref.right and not front.right):
                    match = False
                    break
                
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
                if front_ref.left:
                    q_ref.append(front_ref.left)
                if front_ref.right:
                    q_ref.append(front_ref.right)
            
            if match and not q and not q_ref:
                return True
            
        return False
    
    def pre_order(self, node, sub_val, arr):
        if node:
            if node.val == sub_val:
                arr.append(node)
            self.pre_order(node.left, sub_val, arr)
            self.pre_order(node.right, sub_val, arr)
        