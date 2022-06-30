#https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
#863. All Nodes Distance K in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.output = []
        self.dfs(root, None)
        self.dfs_graph(target, k, set())
        return self.output
    
    
    def dfs_graph(self, node, k, visited):
        if not node or k < 0 or node in visited:
            return
        
        if k == 0:
            self.output.append(node.val)
            return
        
        visited.add(node)
        
        for adj in [node.parent, node.left, node.right]:
            if adj not in visited:
                self.dfs_graph(adj, k-1, visited)
        
    
    def dfs(self, node, parent):
        if not node:
            return
        node.parent = parent
        self.dfs(node.left, node)
        self.dfs(node.right, node)
        