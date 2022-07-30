#https://leetcode.com/problems/minimum-height-trees/
#310. Minimum Height Trees


from collections import defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [x for x in range(n)]
        
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            
        
        leaves = [key for key, val in graph.items() if len(val) == 1]
        
        remaining_nodes = n
        
        while remaining_nodes > 2: # Centroid nodes according to the explanation in the solution tab. 
            
            remaining_nodes -= len(leaves)
            
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop(0)    
                adj = graph[leaf].pop()
                graph[adj].remove(leaf)
                if len(graph[adj]) == 1:
                    new_leaves.append(adj)

            leaves = new_leaves
        
        return leaves
            
            
            
        
        