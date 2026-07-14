class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_profit = 0
        length = len(prices)
        for i in range(length): 
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit
        