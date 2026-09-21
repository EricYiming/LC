class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def canFinish(piles, k, h): 
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            return count <= h

        while l < r: 
            mid = (l + r) // 2
            if canFinish(piles, mid, h): 
                r = mid
            else: 
                l = mid + 1
        return r
        

        
        