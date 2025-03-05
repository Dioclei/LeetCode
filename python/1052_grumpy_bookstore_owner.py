from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        p1 = 0
        p2 = p1 + (minutes - 1)
        # first pass calculate satisfaction when p1 = 0
        satisfaction = 0
        for i in range(len(customers)):
            if i <= p2 or not grumpy[i]:
                satisfaction += customers[i]
        max_satisfaction = satisfaction

        p1, p2 = p1 + 1, p2 + 1
        while p2 < len(customers):
            # calculate new satisfaction
            # p1
            if grumpy[p1-1]:
                satisfaction -= customers[p1-1]
            # p2
            if grumpy[p2]:
                satisfaction += customers[p2]
            max_satisfaction = max(max_satisfaction, satisfaction)
            p1, p2 = p1 + 1, p2 + 1

        return max_satisfaction
    
sol = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
print(sol.maxSatisfied(customers, grumpy, 3))