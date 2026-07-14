class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n): 
            max_sub = 1
            for j in range(i): 
                if nums[j] < nums[i]: 
                    max_sub = max(max_sub, dp[j] + 1)

            dp[i] = max(dp[i], max_sub)
        return max(dp)        