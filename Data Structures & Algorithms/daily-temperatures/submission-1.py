class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            temp = temperatures[i] 
            while stack and stack[-1][0] < temp: 
                val, ind = stack.pop()
                res[ind] = i - ind
            
            stack.append([temp, i])

        return res

        