class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        n = len(nums)
        res = []

        def dfs(i): 
            if i == n: 
                res.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            while i < n - 1 and nums[i] == nums[i + 1]: 
                i += 1
            if i < n: 
                dfs(i + 1)
            return
        dfs(0)
        return res
            
        