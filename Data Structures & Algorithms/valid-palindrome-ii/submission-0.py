class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right: 
            if s[left] == s[right]: 
                left += 1
                right -= 1
            else: 
                rid_left = s[left + 1: right + 1]
                rid_right = s[left: right]
                return rid_left == rid_left[::-1] or rid_right == rid_right[::-1]
        return True

        