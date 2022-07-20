#https://leetcode.com/problems/01-matrix/
#542. 01 Matrix
# In all honesty the solutions below are from the solutions tab in leetcode. This problem was a grean learning experience. 


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.ROWS = len(mat)
        self.COLS = len(mat[0])
        dist = [ [float('inf')] * self.COLS for x in range(self.ROWS)]
        
        q = []
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        
        while q: 
            i, j = q.pop(0)
            for a, b in self.get_adjacents(i, j):
                if dist[a][b] > dist[i][j] + 1:
                    dist[a][b] = dist[i][j] + 1
                    q.append((a, b))
                    
        return dist

    def get_adjacents(self, i, j):
        adjs = []
        for x, y in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if 0 <= x < self.ROWS and 0 <= y < self.COLS:
                adjs.append((x, y))
        
        return adjs          

################# An even better solution using dynamic programming ##############

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.ROWS = len(mat)
        self.COLS = len(mat[0])
        dist = [ [float('inf')] * self.COLS for x in range(self.ROWS)]
        
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
        
        for i in range(self.ROWS - 1, -1, -1):
            for j in range(self.COLS -1, -1, -1):
                if i < self.ROWS - 1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < self.COLS - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
                                    
        return dist

