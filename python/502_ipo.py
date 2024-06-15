from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # sort capital in ascending order
        capital_profit = sorted(zip(capital, profits), key=lambda x: x[0])
        # create a max pq to store possible profits
        pq = []
        # pointer to indicate largest profit
        p = 0
        while k > 0:
            # increment pointer until maximal capital
            while p < len(capital_profit) and capital_profit[p][0] <= w:
                # capture the profit and push into pq
                profit = capital_profit[p][1]
                heapq.heappush(pq, -profit)
                # increment p
                p += 1
            # if there is no more purchasable stock, break the loop
            if len(pq) == 0:
                break
            # take maximum profit and pop from pq, update capital
            max_profit = heapq.heappop(pq) * -1
            w += max_profit
            k -= 1
        return w

profits = [1, 2, 3]
capital = [0, 1, 1]
k = 2
w = 0
print(Solution().findMaximizedCapital(k, w, profits, capital))
        
