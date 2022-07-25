#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


################# Backtracking recursive DFS approach #################

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ances = self.get_ances(root, p, [])
        q_ances = self.get_ances(root, q, [])
        n = min(len(p_ances), len(q_ances))
        lca = None
        for i in range(n):
            if p_ances[i] == q_ances[i]:
                lca = p_ances[i]
            else:
                break
                
        return lca
    
    def get_ances(self, root, node, ances):
        if root == node:
            ances.append(node)
            return ances
        
        for child in [root.left, root.right]:
            if child:
                ances.append(root)
                result = self.get_ances(child, node, ances)
                if result:
                    return result
                ances.remove(root)


################################## BFS Iterative approach ##################################

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ances = self.get_ances(root, p, [])
        q_ances = self.get_ances(root, q, [])
        n = min(len(p_ances), len(q_ances))
        lca = None
        for i in range(n):
            if p_ances[i] == q_ances[i]:
                lca = p_ances[i]
            else:
                break
                
        return lca
        
    
    def get_ances(self, root, node, ances):
        if root == node:
            return [root]
        q = []
        q.append((root, []))
        while q:
            front, ances = q.pop(0)
            ances.append(front)
            for child in [front.left, front.right]:
                if child:
                    if child == node:
                        ances.append(child)
                        return ances
                    q.append((child, ances))