class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        # dp[no. of houses (0 indexed)] = (max value, whether last house is robbed) for:
        # 1. if first house is robbed
        dp_1 = [None] * len(nums)
        dp_1[0] = (nums[0], True)
        i = 1
        while i < len(nums) - 1:
            last = dp_1[i - 1]
            if not last[1]:
                # last house was not robbed so rob this one
                dp_1[i] = (last[0] + nums[i], True)
            elif i != 1 and dp_1[i - 2][0] + nums[i] > dp_1[i - 1][0] :
                # last house was robbed and robbing the new house is better
                # add exception for i = 1 because we need to make sure that the first house is robbed
                dp_1[i] = (dp_1[i - 2][0] + nums[i], True)
            else:
                dp_1[i] = (last[0], False)
            i += 1
        dp_1[i] = dp_1[i - 1]
        print(dp_1)

        # 2. if first house is not robbed
        dp_2 = [None] * len(nums)
        dp_2[0] = (0, False)
        j = 1
        while j < len(nums):
            last = dp_2[j - 1]
            if not last[1]:
                # last house was not robbed so rob this one
                dp_2[j] = (last[0] + nums[j], True)
            elif dp_2[j - 2][0] + nums[j] > dp_2[j - 1][0]:
                # robbing the new house is better
                dp_2[j] = (dp_2[j - 2][0] + nums[j], True)
            else:
                dp_2[j] = (last[0], False)
            j += 1
        print(dp_2)
        
        # compare the two outcomes and choose the larger one
        out1 = dp_1[-1][0]
        out2 = dp_2[-1][0]
        return max(out1, out2)
    
def test():
    s = Solution()
    r = s.rob([2,3,2])
    print(r)

test()