# hard

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # 3 actions on every day - buy, sell, do nothing
        # if i recurse everyday it will be O(3^n) ...
        # if i calculate the potential profit of every transaction it will be O(n^2) ...
        # i only have 2 transactions!
        # if i only have 1 transaction, I run the O(n) algorithm in 121 to find the best valley and peak
        # since i have 2 transactions, I can choose a split and run the O(n) algorithm two separate times, this is O(n^2)
        # this is a top-down approach, for dp we want to do a bottom-up approach

        # is there a way to simplify it?
        # for instance, if i solve the problem for 2 days, can i solve the problem for 3 days more easily?
        # by solving the problem for 2 days, i should not need to consider the same dead paths for 3 days

        # keep track of all days' best 1-transaction profit, 
        # and use that to calculate best 2-transaction profit for each day
        # but how???
        # what do i need..?

        # idea: calculate valleys and peaks
        # valleys < peaks. so a after buying at a valley i you can sell at peak i
        # but after selling at peak i you cannot buy at valley i

        n = len(prices)
        valleys = []
        peaks = []
        profit = []
        # check if first value is a valley
        if prices[0] < prices[1]:
            valleys.append(0)
        for i in range(1, n - 1):
            if prices[i - 1] >= prices[i] and prices[i] < prices[i + 1]:
                valleys.append(i)
            elif prices[i - 1] <= prices[i] and prices[i] > prices[i + 1]:
                peaks.append(i)
        # check if last value is a peak
        if prices[-1] > prices[-2]:
            peaks.append(n - 1)
        # calculate profit for each pairing
        for i in range(len(valleys)):
            p = valleys[i]
            q = peaks[i]
            profit.append(prices[q] - prices[p])

        print((valleys, peaks, profit))
        
        # i give up, i'm going to look at the answer
        raise NotImplementedError
    


        
        
        
        

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))


            







