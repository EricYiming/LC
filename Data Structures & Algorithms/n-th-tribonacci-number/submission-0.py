class Solution:
    def tribonacci(self, n: int) -> int:
        t = deque()
        t.append(0)
        t.append(1)
        t.append(1)
        if n < 3: 
            return t[n]
        for i in range(3, n):  
            t.append(t[0] + t[1] + t[2])
            t.popleft()

        return sum(t)