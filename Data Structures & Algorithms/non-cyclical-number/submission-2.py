class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def next(val): 
            res = 0
            while val != 0: 
                res += (val % 10) **2
                val = val // 10
            return res
        
        while n != 1: 
            if n in seen: 
                return False
            else: 
                seen.add(n)
                n = next(n)


        return True

        