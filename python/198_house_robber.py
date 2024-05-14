# medium

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [None] * (len(nums) + 1)
        # dp[n] = (maximum value, whether last house was robbed) at n houses
        dp[0] = (0, False)

        def rob_n(n):
            if n > len(nums): return
            if dp[n - 1][1] == False:
                # if prev house was not robbed, then rob the next house. guaranteed to be new maximum
                max = dp[n - 1][0] + nums[n - 1]
                dp[n] = (max, True)
            else:
                # if prev house was robbed, then choose between:
                # not robbing the new house, or 
                m1 = dp[n - 1][0]
                # robbing the new house instead of the prev house
                m2 = dp[n - 2][0] + nums[n - 1]
                if m1 > m2:
                    dp[n] = (m1, False)
                else:
                    dp[n] = (m2, True)
            rob_n(n + 1)
        rob_n(1)
        return dp[len(nums)][0]





