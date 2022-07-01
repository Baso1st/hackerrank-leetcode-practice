#https://leetcode.com/problems/design-tic-tac-toe/
#348. Design Tic-Tac-Toe

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board_1 = [[0]*n for i in range(n)]
        self.board_2 = [[0]*n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.board_1[row][col] = 1
            if self.is_a_win(row, col, self.board_1):
                return player
        elif player == 2:
            self.board_2[row][col] = 1
            if self.is_a_win(row, col, self.board_2):
                return player 
            
        return 0
    
    def is_a_win(self, row, col, board):
        n = len(board)
        if sum(board[row]) == n:
            return True
        
        col_sum = sum([row[col] for row in board])
        if col_sum == n:
            return True
        
        dia_sum = sum([board[i][i] for i in range(n)])
        if dia_sum == n:
            return True
        
        rev_dia_sum = sum([board[i][(n-1)-i] for i in range(n)])
        if rev_dia_sum == n:
            return True
        
        return False
            
###################################################################

class Player:
    def __init__(self, name, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.dia = 0
        self.rev_dia = 0
    
    def is_a_winner(self, row, col):
        self.rows[row] += 1
        if self.rows[row] == self.n:
            return True
        self.cols[col] += 1
        if self.cols[col] == self.n:
            return True
        if row == col:
            self.dia += 1
        if self.dia == self.n:
            return True
        if row == ((self.n-1) - col):
            self.rev_dia += 1
        if self.rev_dia == self.n:
            return True
        return False

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.players = [Player(1, n), Player(2, n)]

    def move(self, row: int, col: int, player: int) -> int:
        if self.players[player-1].is_a_winner(row, col):
            return player
        return 0

            
    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)