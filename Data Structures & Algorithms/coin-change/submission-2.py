class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9] * (amount + 1)
        dp[0] = 0
        for val in range(1, amount + 1): 
            for coin in coins: 
                if val - coin >= 0: 
                    dp[val] = min(1 + dp[val - coin], dp[val])
        return dp[amount] if dp[amount] != 1e9 else -1