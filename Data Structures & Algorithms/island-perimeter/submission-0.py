class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        count = 0
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(num_row): 
            for c in range(num_col): 
                if grid[r][c] == 1: 
                    for move in moves: 
                        nr = r + move[0]
                        nc = c + move[1]
                        if nr < 0 or nr >= num_row or nc < 0 or nc >= num_col or grid[nr][nc] == 0: 
                            count += 1
        return count

        