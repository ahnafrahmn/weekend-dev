class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        mi , profit, i = prices[0], 0, 0
        while i < len(prices):
            if prices[i] < mi:
                mi = prices[i]
            elif profit < prices[i]-mi:
                profit = prices[i]-mi
            i += 1
        return profit