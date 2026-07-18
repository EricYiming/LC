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

            total += candidates[i]
            path.append(candidates[i])
            dfs(i + 1, total)
            path.pop()
            total -= candidates[i]

            while i + 1 < n and candidates[i + 1] == candidates[i]: 
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res
