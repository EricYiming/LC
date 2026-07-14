class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        grid = [[0] * n for _ in range(n)]
        count = 0

        for i in range(n - 1, -1, -1): 
            for j in range(i, n): 
                if i == j: 
                    grid[i][j] = 1
                    count += 1
                else: 
                    if s[i] == s[j] and (grid[i + 1][j - 1] == 1 or i + 1 >= j  - 1): 
                        grid[i][j] = 1
                        count += 1
        return count

        