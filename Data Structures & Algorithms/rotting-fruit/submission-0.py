class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        
        q = deque()
        for r in range(num_row): 
            for c in range(num_col): 
                if grid[r][c] == 2:
                    q.append((r, c))
        max_time = 0
        while q: 
            r, c = q.popleft()
            moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for move in moves: 
                nr = r + move[0]
                nc = c + move[1]
                if 0 <= nr < num_row and 0 <= nc < num_col and grid[nr][nc] == 1: 
                    grid[nr][nc] = grid[r][c] + 1
                    max_time = max(grid[nr][nc] - 2, max_time)
                    q.append((nr, nc))
        
        for r in range(num_row): 
            for c in range(num_col): 
                if grid[r][c] == 1:
                    return -1         
        return max_time