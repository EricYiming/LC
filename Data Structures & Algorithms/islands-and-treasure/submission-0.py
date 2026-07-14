class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_row = len(grid)
        num_col = len(grid[0])
        INF = 2147483647
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        
        for r in range(num_row): 
            for c in range(num_col): 
                if grid[r][c] == 0: 
                    q.append((r, c))
        while q: 
            r, c = q.popleft()

            for move in moves: 
                nr = r + move[0]
                nc = c + move[1]

                if nr >= 0 and nr < num_row and nc >= 0 and nc < num_col and grid[nr][nc] == INF: 
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
            
                


