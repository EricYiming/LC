class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf") for i in range(n)]

        for i in range(n - 1, -1, -1): 
            if i == n - 1: 
                dp[i] = 0
                continue

            bound = min(n - 1, i + nums[i])
            min_step = float("inf")
            for j in range(i + 1, bound + 1): 
                min_step = min(min_step, dp[j])
            dp[i] = min_step + 1

        return dp[0]

                      
        