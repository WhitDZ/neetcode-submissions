class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices) - 1, 0 , -1):
            sell = prices[i]
            buy = min(prices[0:i])
            profit = sell - buy
            if best_profit <  profit:
                best_profit = profit
        return best_profit
