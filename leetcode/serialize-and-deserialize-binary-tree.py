#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#297. Serialize and Deserialize Binary Tree
# Below is my solution, It uses BFS. LeetCode solution tab has a DFS solution that's worth looking at as well. 

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        output = []
        q = deque()
        q.append(root)
        while q:
            front = q.popleft()
            if not front:
                output.append(None)
                continue
            output.append(front.val)
            q.append(front.left)
            q.append(front.right)
        
        while output[-1] == None:
            output.pop()
        return str(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        
        vals = deque(eval(data))
        
        root = TreeNode(vals.popleft())
        q = deque()
        q.append(root)
        while q and vals:
            node = q.popleft()
            left_val = vals.popleft()
            if left_val != None:
                node.left = TreeNode(left_val)
                q.append(node.left)
            if vals:
                right_val = vals.popleft()
                if right_val != None:
                    node.right = TreeNode(right_val)
                    q.append(node.right)
            
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))