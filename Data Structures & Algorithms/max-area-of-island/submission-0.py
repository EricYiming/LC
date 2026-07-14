class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        num_row = len(grid)
        num_col = len(grid[0])

        max_area = 0

        def dfs(r, c): 
            if r < 0 or r >= num_row or c < 0 or c >= num_col or grid[r][c] == 0: 
                return 0
            grid[r][c] = 0
            return 1 + dfs(r, c + 1) + +dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
        
        for r in range(num_row): 
            for c in range(num_col): 
                area = dfs(r, c)
                max_area = max(max_area, area)
        return max_area
            
            
        