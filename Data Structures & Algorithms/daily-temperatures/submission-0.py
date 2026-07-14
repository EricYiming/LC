class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n): 
            cur = temperatures[i]
            while stack and cur > stack[-1][0]: 
                index = stack[-1][1]
                res[index] = i - index
                stack.pop()
            stack.append([cur, i])
        return res
            


        