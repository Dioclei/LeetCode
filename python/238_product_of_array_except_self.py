# medium

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l = len(nums)
        answer = [1] * l
        m = nums[0]
        p = 1
        while p < l:
            answer[p] = m
            m *= nums[p]
            p += 1
        p = l - 2
        m = nums[-1]
        while p >= 0:
            answer[p] *= m
            m *= nums[p]
            p -= 1
        return answer
