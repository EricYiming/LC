class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def hourNeeded(speed):
            count = 0
            for pile in piles: 
                if pile % speed == 0: 
                    count += pile / speed
                else: 
                    count += pile // speed + 1
            return count


        left, right = 1, max(piles)

        while left < right: 
            mid = left + (right - left) // 2

            hours = hourNeeded(mid)
            if hours <= h: 
                right = mid
            else: 
                left = mid + 1
            
        return left




        