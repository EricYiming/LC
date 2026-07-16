class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(n): 
            if n == len(nums): 
                res.append(path.copy())
                return
            dfs(n + 1)
            path.append(nums[n])
            dfs(n + 1)
            path.pop()
        dfs(0)
        return res
            
        