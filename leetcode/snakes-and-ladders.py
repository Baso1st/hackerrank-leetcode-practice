#https://leetcode.com/problems/snakes-and-ladders/
#909. Snakes and Ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        adjacency = [None] * ((n**2))
        
        portals = {}
        
        node = 0
        board.reverse()
        for i, row in enumerate(board):
            if i % 2 != 0:
                row.reverse()
            for j, col in enumerate(row):
                adjacency[node] = [x for x in range(node+1, min(node+7 , (n**2)) )]
                if board[i][j] > -1:
                    portals[node] = board[i][j] - 1
                node += 1
        
        
        for adj in adjacency:
            for i, val in enumerate(adj):
                if val in portals:
                    adj[i] = portals[val]
        

        shortest_dist = [float('inf')] * ((n**2))
        q = []
        q.append((0, 0))
        while q:
            parent_dist, node = q.pop(0)
            for adj in adjacency[node]:
                if shortest_dist[adj] > parent_dist + 1:
                    shortest_dist[adj] = parent_dist + 1
                    q.append((shortest_dist[adj], adj))
        
        result = shortest_dist[(n**2) - 1]
        return result if result < float('inf') else -1