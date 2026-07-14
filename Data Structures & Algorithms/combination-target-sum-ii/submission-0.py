class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        n = len(candidates)

        def dfs(i, total): 
            if total == target: 
                res.append(path.copy())
                return
            if i == n or total > target: 
                return 
            else: 
                path.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                path.pop()

                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]: 
                    i += 1
                dfs(i + 1, total)

        dfs(0, 0)
        return list(res)