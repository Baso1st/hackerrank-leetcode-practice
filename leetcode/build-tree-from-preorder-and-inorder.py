#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#105. Construct Binary Tree from Preorder and Inorder Traversal



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        idx_table = {}
        
        for i, val in enumerate(inorder):
            idx_table[val] = i
            
        for val in preorder[1:]:
            current = root
            val_in_idx = idx_table[val]
            while current:
                curr_in_idx = idx_table[current.val]
                if val_in_idx < curr_in_idx:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(val)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(val)
                        break
        return root


############################################### A better solution from the leetcode solutions tab #####################################################


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder_map = {}
        self.root_pre_idx = 0
        for i, val in enumerate(inorder):
            self.inorder_map[val] = i
            
        return self.arr_to_tree(0, 0, len(preorder)-1)
        
    
    def arr_to_tree(self, root_pre_idx, left, right):
        if left > right:
            return
        
        root_val = self.preorder[self.root_pre_idx]
        root = TreeNode(root_val)
        
        self.root_pre_idx += 1
        
        root_in_idx = self.inorder_map[root_val]
        root.left = self.arr_to_tree(root_pre_idx + 1, left, root_in_idx-1)
        root.right = self.arr_to_tree(root_pre_idx + 1, root_in_idx + 1, right)
        
        
        return root