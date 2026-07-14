class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x

        while left < right: 
            mid = left + (right - left) // 2 + 1

            square = mid * mid

            if square == x: 
                return mid
            elif square < x: 
                left = mid
            else: 
                right = mid - 1
        
        return left
        