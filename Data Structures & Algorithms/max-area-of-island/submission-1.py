class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        num_row = len(grid)
        num_col = len(grid[0])
        MOVES = [[1, 0], [-1, 0], [0, 1], [0, -1]]



        def dfs(r, c): 
            if r >= num_row or r < 0 or c >= num_col or c < 0 or grid[r][c] == 0: 
                return 

            nonlocal count 
            grid[r][c] = 0
            count += 1       
            for move in MOVES: 
                nr = r + move[0]
                nc = c + move[1]
                dfs(nr, nc)
        
        count = 0 
        result = 0    

        for r in range(num_row): 
            for c in range(num_col): 
                count = 0
                dfs(r, c)   
                result = max(result, count)
        return result    
        