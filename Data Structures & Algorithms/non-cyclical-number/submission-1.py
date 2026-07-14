class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        def happy(n): 
            total = 0
            while n >= 10: 
                dig = n % 10
                total += dig * dig
                n = n // 10
            total += n * n
            return total

        while True: 
            n = happy(n)
            if n == 1: 
                return True
            if n in seen: 
                return False
            seen.add(n)
        