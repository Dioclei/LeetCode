from typing import List

class Solution:
    # this is a terribly organised solution.. see below for editorial solution
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        p1 = 0
        p2 = len(nums) - 1
        while p2 >= 0 and nums[p2] == val:
            p2 -= 1
        while p1 < p2:
            print(nums)
            if nums[p1] == val:
                # swap
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                while nums[p2] == val:
                    p2 -= 1
            else:
                p1 += 1
        for i in range(len(nums)):
            if nums[i] == val:
                return i
        return len(nums)
    
    
    # editorial solution
    # editorial solution doesn't try to change both pointers at the same time. I think this is a good rule to follow. keep it simple.

    # def removeElement(self, nums: List[int], val: int) -> int:
    # i = 0
    # n = len(nums)
    # while i < n:
    #     if nums[i] == val:
    #         nums[i] = nums[n - 1]
    #         n -= 1
    #     else:
    #         i += 1
    # return n
        
sol = Solution()
l = [4,2,0,2,2,1,4,4,1,4,3,2]
print(sol.removeElement(l, 4))
print(l)
