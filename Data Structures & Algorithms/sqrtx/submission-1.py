class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        while l < r: 
            mid = (l + r) // 2 + 1
            res = mid ** 2

            if res > x: 
                r = mid - 1
            else: 
                l = mid
        
        return l
        