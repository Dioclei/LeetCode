class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        # O(n)

        seconds = 0
        m = tickets[k]
        for i in range(len(tickets)):
            t = tickets[i]
            if i <= k:
                seconds += min(t, m)
            else:
                seconds += min(t, m - 1)
        return seconds

        
        # O(kn)
        
        # seconds = 0
        # p = 0
        # l = len(tickets)
        # while tickets[k] > 0:
        #     if tickets[p] > 0:
        #         tickets[p] = tickets[p] - 1
        #         seconds = seconds + 1
        #     p = (p + 1) % l

        # return seconds

def test():
    s = Solution()
    print(s.timeRequiredToBuy([2,3,2], 2))

test()