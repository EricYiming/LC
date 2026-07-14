class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        num_row, num_col = len(grid), len(grid[0])

        def dfs(r, c): 
            if r < 0 or r >= num_row or c < 0 or c >= num_col or grid[r][c] == '0': 
                return
            grid[r][c] = '0'
            for move in moves: 
                nr = r + move[0]
                nc = c + move[1]
                dfs(nr, nc)
                
        for r in range(num_row): 
            for c in range(num_col): 
                if grid[r][c] == '1': 
                    dfs(r, c)
                    count += 1
        return count


        