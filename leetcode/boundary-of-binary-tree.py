#https://leetcode.com/problems/boundary-of-binary-tree/
#545. Boundary of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        return self.get_boundary(root)
        
        
    def get_boundary(self, root):
        left_boundary = []
        if root.left:
            node = root.left
            while node:
                left_boundary.append(node)
                if node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                else:
                    node = None
        
        right_boundary = []
        if root.right:
            node = root.right
            while node:
                right_boundary.append(node)
                if node.right:
                    node = node.right
                elif node.left:
                    node = node.left
                else:
                    node = None
                    
        right_boundary.reverse()
        
        result_dict = dict.fromkeys([root] + left_boundary + self.get_leaves_dfs(root) + right_boundary)        
        return  [x.val for x in result_dict.keys()]
        
    
    def get_leaves_dfs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root]
        
        leaves = []
        if root.left:
            leaves += self.get_leaves_dfs(root.left)
        if root.right:
            leaves += self.get_leaves_dfs(root.right)
        
        return leaves
            
        