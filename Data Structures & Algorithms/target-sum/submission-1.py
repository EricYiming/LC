class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (target + total) % 2 != 0: 
            return 0
        
        aim = (target + total) // 2
        dp = [0] * (aim + 1)
        dp[0] = 1

        for x in nums: 
            for attempt in range(aim, x - 1, -1): 
                dp[attempt] += dp[attempt - x]
        return dp[aim]