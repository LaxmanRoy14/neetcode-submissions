class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_profit = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > cheapest:
                profit = prices[i] - cheapest
            cheapest = min(cheapest, prices[i])
            max_profit = max(max_profit, profit)
        return max_profit

