#https://leetcode.com/problems/number-of-islands/
#200. Number of Islands

from ast import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':   
                    continue
                islands += 1
                self.dfs(i, j, grid)
                    
        return islands 
            
        
    def dfs(self, i, j, grid):
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        adjs = self.get_adjacent(i, j, grid)
        for adj in adjs:
            self.dfs(adj[0], adj[1], grid)
                
    
    def get_adjacent(self, i, j, grid):
        adjacent = []
        
        if i > 0 and grid[i-1][j] == '1':
            adjacent.append((i-1, j))
        if i < (len(grid)-1) and grid[i+1][j] == '1':
            adjacent.append((i+1, j))
        if j > 0 and grid[i][j-1] == '1':
            adjacent.append((i, j-1))
        if j < (len(grid[i])-1) and grid[i][j+1] == '1':
            adjacent.append((i, j+1))
        
        return adjacent
                    
    
    