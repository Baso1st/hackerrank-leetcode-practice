#https://leetcode.com/problems/rotting-oranges/
#994. Rotting Oranges


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        rotten = []
        self.fresh_count = 0
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    self.fresh_count += 1
        
        if not rotten and not self.fresh_count:
            return 0
        
        minutes = self.decay(grid, rotten, 0)
        
        if self.fresh_count > 0:
            return -1       
        
        return minutes -1 
        
    def decay(self, grid, rotten, minutes):
        if not rotten:
            return minutes
        
        new_rotten = []
        while rotten:
            i, j = rotten.pop(0)
            adjacent = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]
            for adj in ( x for x in adjacent if 0 <= x[0] < self.ROWS and 0 <= x[1] < self.COLS):
                i, j = adj
                if grid[i][j] == 1:
                    new_rotten.append(adj)
                    grid[i][j] = 2
                    self.fresh_count -= 1
                    
        return self.decay(grid, new_rotten, minutes + 1)
                
                    