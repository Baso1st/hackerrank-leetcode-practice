#https://leetcode.com/problems/course-schedule-ii/
#210. Course Schedule II
#Topological Sorted Order

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [None] * numCourses
        self.visited = [False] * numCourses
        self.result = []
        self.cycle = False
        
        for preq in prerequisites:
            if self.graph[preq[0]]:
                self.graph[preq[0]].append(preq[1])
            else:
                self.graph[preq[0]] = [preq[1]]
                

        for i in range(numCourses):
            if self.cycle:
                break
            if self.visited[i]:
                continue       
                
            if self.graph[i] == None and not self.visited[i]:
                self.result.append(i)
                self.visited[i] = True
                
            self.dfs(i, set())
        
        
        if self.cycle:
            return []
        
        return self.result
        
    def dfs(self, i, ancestors):
        if self.visited[i] or self.cycle:
            return
        
        if self.graph[i]:
            ancestors.add(i)
            for pre in self.graph[i]:
                if pre in ancestors:
                    self.cycle = True
                    return 
                self.dfs(pre, set(ancestors))
            
        self.result.append(i)
        self.visited[i] = True


############################ A Better solution found in the solution tab at leetcode. #######################

from collections import defaultdict 
class Solution:
    Pristine = 1
    Touched = 2
    Explored = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        self.state = {k: Solution.Pristine for k in range(numCourses)}
        self.result = []
        self.cycle = False
        print(self.state)
        for child, parent in prerequisites:
            self.graph[parent].append(child)
            
        for i in range(numCourses):
            if self.cycle:
                break
            if self.state[i] == Solution.Pristine:
                self.dfs(i)
        
        if self.cycle:
            return []
        
        return self.result[::-1]
        
    
    def dfs(self, node):
        if self.state[node] == Solution.Explored or self.cycle:
            return
        
        self.state[node] = Solution.Touched
        if node in self.graph:
            for adj in self.graph[node]:
                if self.state[adj] == Solution.Pristine:
                    self.dfs(adj)
                elif self.state[adj] == Solution.Touched:
                    self.cycle = True
                    return
        
        self.state[node] = Solution.Explored
        self.result.append(node)
                
        
        
        