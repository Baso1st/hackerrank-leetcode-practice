
#binary-tree-right-side-view
#199. Binary Tree Right Side View



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.recurse(root, 0)
        return self.result
        
    def recurse(self, node, level):
        if not node:
            return
        if level >= len(self.result):
            self.result.append(node.val)
        else:
            self.result[level] = node.val
        
        self.recurse(node.left, level+1)
        self.recurse(node.right, level+1)