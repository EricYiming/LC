class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr, nc = len(grid), len(grid[0])
        MOVES = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0



        def dfs(r, c): 
            if r >= nr or c >= nc or r < 0 or c < 0 or grid[r][c] == '0': 
                return
            grid[r][c] = '0'
            for move in MOVES: 
                rp = r + move[0]
                cp = c + move[1]
                dfs(rp, cp)

        for r in range(nr): 
            for c in range(nc): 
                if grid[r][c] == '1': 
                    count += 1
                    dfs(r, c)
        return count
        




            

        