#https://leetcode.com/problems/word-search/
#79. Word Search

class Solution:
    def __init__(self):
        self.found_it = False
        
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        row_len = len(board[0])
        
        if len(word) > n*row_len:
            return False
        
        the_set = set()
        
        for i in range(n):
            for j in range(len(board[i])):
                the_set.add(board[i][j])
        
        for c in word:
            if c not in the_set:
                return False
                
        for i in range(n):
            for j in range(len(board[i])):
                if self.found_it:
                    return True
                if board[i][j] == word[0]:
                    visited = []
                    self.dfs(i, j, board, visited, word[1:])
        
        return self.found_it
        
    
    def dfs(self, i, j, board, visited, word):
        if self.found_it:
            return
        
        if [i, j] in visited:
            return
        
        visited.append([i, j])
        if len(word) == 0:
            self.found_it = True
            return
                
        for adj in self.get_adjacent(i, j, board):
            if board[adj[0]][adj[1]] == word[0]:
                while visited[-1] != [i, j]:
                    visited.pop()
                if [adj[0], adj[1]] not in visited:
                    self.dfs(adj[0], adj[1], board, visited, word[1:])
        

    
    def get_adjacent(self, i, j, board):
        adjacents = []
        if i > 0:
            #Top
            adjacents.append([i-1, j])
        if j > 0:
            #Left
            adjacents.append([i, j-1])
        if i+1 < len(board):
            #Bottom
            adjacents.append([i+1, j])
        if j+1 < len(board[i]):
            #Right
            adjacents.append([i, j+1])
        return adjacents
            

################################### A better solution influnced by LeetCode solutions tab####################################

class Solution:

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.BOARD = board
        
        if len(word) > self.ROWS * self.COLS:
            return False
        
        if not self.verify_all_chars(word):
            return False
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.backtrack(i, j, word):
                    return True
                
        return False
        
    
    def verify_all_chars(self, word):
        char_set = set()
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                char_set.add(self.BOARD[i][j])
        
        for c in word:
            if c not in char_set:
                return False
            
        return True
    
    def backtrack(self, i, j, word):
        if len(word) == 0:
            return True
        
        
        if i < 0 or j < 0 or i >= self.ROWS or j >= self.COLS or self.BOARD[i][j] != word[0]:
            return False
    
        self.BOARD[i][j] = '#'
        
        found_it = False
        for row_offset, col_offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            found_it = self.backtrack(i + row_offset, j + col_offset, word[1:])
            if found_it:
                break
        
        self.BOARD[i][j] = word[0]
        
        return found_it 
        
            

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    s = Solution()
    print(s.exist(board, word))