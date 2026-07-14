class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def dfs(i, total): 
            if i == n or total > target: 
                return 
            if total == target: 
                res.append(path.copy())
                return
            for idx in range(i, n): 
                path.append(nums[idx])
                dfs(idx, total + nums[idx])
                path.pop()
        dfs(0, 0)
        return res
                
            