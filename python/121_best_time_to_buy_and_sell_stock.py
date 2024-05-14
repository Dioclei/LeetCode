class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # trying to do O(n)

        # go thru the prices to find a buy price
        # if lower than current buy price, take the new one
        # if higher than current sell price, take the new one and calculate the profit
        # since we cannot sell in the past and buy in the future, 
        # we should cache the profit and only update it when sell price is updated
        
        buy_price = 9999999
        sell_price = 0
        profit = 0
        for p in prices:
            if p < buy_price:
                buy_price = p
                # find new sell price
                sell_price = 0
            elif p > sell_price:
                sell_price = p
                new_profit = sell_price - buy_price
                profit = new_profit if new_profit > profit else profit
        return profit
