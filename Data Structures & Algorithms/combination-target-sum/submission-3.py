class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        def dfs(i, total): 
            if i == len(nums): 
                if total == target: 
                    res.append(path.copy())
                return
            elif total == target: 
                res.append(path.copy())
                return
            elif total > target:
                return
            else: 
                total += nums[i]
                path.append(nums[i])
                dfs(i, total)
                total -= nums[i]
                path.pop()
                dfs(i + 1, total)
        
        dfs(0, 0)
        return res


                
        