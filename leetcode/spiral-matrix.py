#https://leetcode.com/problems/spiral-matrix/
#54. Spiral Matrix

class Direction:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3
        
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        result = []
        self.recurse(0,0, Direction.RIGHT, matrix, result)
        result = [matrix[i][j] for i, j in result]
        return result
    
    def recurse(self, i, j, direction, matrix, result):
        if (i, j) in result:
            return
        result.append((i,j))
        a, b, new_dir = self.get_next(i, j, direction, result)
        self.recurse(a, b, new_dir, matrix, result)
            
            
    def get_next(self, i, j, direction, result):
        
        current_dir = direction
        for _ in range(2):
            for a, b, new_dir in [(i, j + 1, Direction.RIGHT), (i, j - 1, Direction.LEFT),
                                  (i+1, j, Direction.DOWN), (i-1, j, Direction.UP)]:
                if 0 <= a < self.ROWS and 0 <= b < self.COLS and (a, b) not in result and current_dir == new_dir:
                    return (a, b, new_dir)
            current_dir = ((direction + 1) % 4)
        
        return (i, j, direction)

############################### A Better solution uses space complexity: O(1) #################################

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        top = 0
        right = cols - 1 
        bottom = rows -1 
        
        while len(result) < (rows * cols):
            for c in range(left, right+1):
                result.append(matrix[top][c])
                
            for r in range(top+1, bottom+1):
                result.append(matrix[r][right])

            if top != bottom:
                for c in range(right-1, left-1, -1):
                    result.append(matrix[bottom][c])
                    
            if left != right:
                for r in range(bottom-1, top, -1):
                    result.append(matrix[r][left])
            
            left += 1
            top += 1
            right -= 1
            bottom -= 1
            
        return result
