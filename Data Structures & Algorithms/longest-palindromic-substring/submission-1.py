class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 1
        best = s[0]
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n): 
            dp[i][i] = True
        
        for length in range(2, n + 1): 
            for l in range(n - length + 1): 
                r = l + length - 1
                if s[l] == s[r]: 
                    if length == 2: 
                        dp[l][r] = True
                    else: 
                        dp[l][r] = dp[l + 1][r - 1]
                else: 
                    dp[l][r] = False
                if dp[l][r]: 
                    if r - l + 1 > res: 
                        res = r - l + 1
                        best = s[l: r + 1]
        return best

        
        