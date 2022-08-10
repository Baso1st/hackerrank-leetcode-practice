#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#108. Convert Sorted Array to Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs_create(0, len(nums), nums)
    
    def dfs_create(self, i, j, nums):
        if i >= j:
            return
        mid = (i + j) // 2
        node = TreeNode(nums[mid])
        left = self.dfs_create(i, mid, nums)
        right = self.dfs_create(mid+1, j, nums)
        node.left = left
        node.right = right
        return node


        