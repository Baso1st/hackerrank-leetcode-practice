#https://leetcode.com/problems/validate-binary-search-tree/
#98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        tree_vals = []
        self.pre_order(root, tree_vals)
        seen = set()
        for val in tree_vals:
            if val in seen:
                return False
            seen.add(val)
        if tree_vals == sorted(tree_vals):
            return True
        return False
        
    
    def pre_order(self, node, tree_vals):
        if not node:
            return
        self.pre_order(node.left, tree_vals)       
        tree_vals.append(node.val)
        self.pre_order(node.right, tree_vals)


############# An annoyingly simpler and faster solution from leetcode solution tab ####################
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            if root.val <= prev:
                return False
            
            prev = root.val
            root = root.right
            
                
        return True