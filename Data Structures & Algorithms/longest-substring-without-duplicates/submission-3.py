class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        seen = {}
        res = 0
        while r < n: 
            if s[r] in seen: 
                l = max(l, seen[s[r]] + 1)
            seen[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res

        