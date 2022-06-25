class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                left_cell = grid[i][j-1] if j > 0 else '0'
                top_cell = grid[i-1][j] if i > 0 else '0'
                cell = grid[i][j]
                if cell == '1' and left_cell == '0' and top_cell == '0':
                    islands += 1
                    
        return islands 
    
    