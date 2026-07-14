class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        dp = [[0] * num_col] * num_row
        for r in range(num_row): 
            for c in range(num_col): 
                if r == 0 and c == 0: 
                    dp[r][c] = grid[0][0]
                else: 
                    if r == 0: 
                        dp[r][c] = dp[r][c - 1] + grid[r][c]
                    elif c == 0: 
                        dp[r][c] = dp[r - 1][c] + grid[r][c]
                    else: 
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[-1][-1]