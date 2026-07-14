class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        n = len(s)
        def expand(a, b): 
            nonlocal start, end
            while a >= 0 and b < n and s[a] == s[b]: 
                a -= 1
                b += 1
            length = b - a + 1 - 2

            if length > end - start + 1: 
                end = b - 1
                start = a + 1
        for i in range(n): 
            expand(i, i)
            expand(i, i + 1)
        return s[start:end + 1]