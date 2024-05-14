# medium

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        for i in range(len(prices) - 1):
            # buy stock today if it's going to rise tomorrow
            if prices[i] < prices[i + 1]:
                profit += (prices[i + 1] - prices[i])
        return profit
        