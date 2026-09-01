class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] > min_price:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)
            else:
                min_price = prices[i]
        return max_profit
