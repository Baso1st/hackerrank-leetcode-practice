#https://leetcode.com/problems/critical-connections-in-a-network/
# The solution below doesn't pass all test cases for performance reasons.
# There is a more effecent way to find the bridges using Tarjan's algorithm,
# Can be found here https://www.geeksforgeeks.org/bridge-in-a-graph/ 

from ast import List


class Graph: 
    def __init__(self):
        self.nodes = []
        self.adjacent = {}
        self.visited_count = 0
        
    def add(self, val):
        self.nodes.append(val)
        self.adjacent[val] = set()
        
    
    def bfs(self, node):
        q = []
        q.append(node)
        visited = len(self.nodes)*[False]
        self.visited_count = 0
        while q:
            front = q.pop(0)
            if not visited[front]:
                visited[front] = True
                self.visited_count += 1
            for adj in self.adjacent[front]:
                if not visited[adj]:
                    visited[adj] = True
                    q.append(adj)
                    self.visited_count += 1
            

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # My approach is to build a graph, write a BFS, revmoe one conn at a time and see if the BFS still visits all nodes. 

        graph = Graph()
        #O(N)
        for i in range(n):
            graph.add(i)
            
        #O(C)
        for conn in connections:
            graph.adjacent[conn[0]].add(conn[1])
            graph.adjacent[conn[1]].add(conn[0])
        

        critical = []
        
        #O(C(C+N))
        for ref_conn in connections:
            graph.adjacent[ref_conn[0]].remove(ref_conn[1])
            graph.adjacent[ref_conn[1]].remove(ref_conn[0])
            
            graph.bfs(ref_conn[0])
            if graph.visited_count < n:
                critical.append(ref_conn) 
            
            graph.adjacent[ref_conn[0]].add(ref_conn[1])
            graph.adjacent[ref_conn[1]].add(ref_conn[0])
            
        
        return critical
            
            