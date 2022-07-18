#https://leetcode.com/problems/flood-fill/
#733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        
        n = len(image)
        m = len(image[0])
        prev_color = image[sr][sc]
        
        q = []
        q.append((sr, sc))
        image[sr][sc] = color
        
        while q:
            (i, j) = q.pop(0)
            for adj in self.get_adjacents(i, j, n, m):
                i, j = adj
                if image[i][j] == prev_color:
                    image[i][j] = color
                    q.append((i, j))
                    
        return image
    
    def get_adjacents(self, i, j, n, m):
        adjs = []
        for cell in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if -1 < cell[0] < n and -1 < cell[1] < m:
                adjs.append(cell)
        return adjs