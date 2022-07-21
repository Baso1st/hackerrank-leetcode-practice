#https://leetcode.com/problems/binary-tree-level-order-traversal/
#102. Binary Tree Level Order Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.bfs(root, 0, result)
        return result

    
    def bfs(self, node, level, result):
        if level == len(result):
            result.append([])

        result[level].append(node.val)

        if node.left:
            self.bfs(node.left, level + 1, result)
        if node.right:
            self.bfs(node.right, level + 1, result)


#################################### An iterative approach, a bit better on the space since there is no recursion #########################

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = []
        q.append((root, 0))
        while q:
            node, level = q.pop(0)
            if level >= len(result):
                result.append([])
                
            result[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
                   
        return result
            
            