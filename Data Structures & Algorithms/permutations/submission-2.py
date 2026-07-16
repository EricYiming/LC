class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        chosen = [False] * n
    
        def dfs(i): 
            if i == n: 
                res.append(path.copy())
                return
            
            for j in range(n): 
                if not chosen[j]: 
                    path.append(nums[j])
                    chosen[j] = True
                    dfs(i + 1)
                    path.pop()
                    chosen[j] = False
        
        dfs(0)
        return res


        