#https://leetcode.com/problems/clone-graph/
#133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        q = []
        new_node = Node(node.val)
        node_table = {}
        node_table[node] = new_node
        q.append(node)
        while q:
            node = q.pop(0)
            for adj in node.neighbors:
                if adj not in node_table:
                    new_adj = Node(adj.val)
                    node_table[adj] = new_adj
                    q.append(adj)
                node_table[node].neighbors.append(node_table[adj])

        return new_node
                 
                 
                    