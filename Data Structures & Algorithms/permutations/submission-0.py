class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        n = len(nums)
        visited = [False] * n 

        def dfs(i): 
            if i == n: 
                res.append(path.copy())
                return
            for j in range(n): 
                if not visited[j]: 
                    path.append(nums[j])
                    visited[j] = True
                    dfs(i + 1)
                    path.pop()
                    visited[j] = False
            
                
        

        dfs(0)
        return res
        