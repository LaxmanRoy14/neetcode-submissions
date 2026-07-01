class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1  # Left is buy, Right is sell
        max_profit = 0

        while r < len(prices):
            # Is the current transaction profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # We found a new, lower price to buy at. 
                # Shift the buy pointer to this new minimum.
                l = r
            
            # Always increment the right pointer to check the next day
            r += 1

        return max_profit