class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0: 
            return False
        else: 
            target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums: 
            temp = dp.copy()
            for attempt in range(x, target + 1): 
                if dp[attempt - x]: 
                    temp[attempt] = True
            
            dp = temp
        return dp[-1]
