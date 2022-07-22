#https://leetcode.com/problems/course-schedule/
#207. Course Schedule

from collections import defaultdict

class GNode:
    def __init__(self):
        self.in_degree = 0
        self.out_nodes = []
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(GNode)
        
        edges = 0
        for pre in prerequisites:
            nex, prev = pre[0], pre[1]
            graph[prev].out_nodes.append(nex)
            graph[nex].in_degree += 1
            edges += 1
        
        no_dep = []
        for key in graph:
            if graph[key].in_degree == 0:
                no_dep.append(key)
            
        
        removed_edges = 0
        while no_dep:
            course = no_dep.pop(0)
            
            for next_course in graph[course].out_nodes:
                graph[next_course].in_degree -= 1
                removed_edges += 1
                if graph[next_course].in_degree == 0:
                    no_dep.append(next_course)
        
        if removed_edges == edges:
            return True
        
        return False