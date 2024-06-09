from typing import List

class Solution:
    # def subarraysDivByK(self, nums: List[int], k: int) -> int:
    #     # calculate prefix sum % k
    #     # if for any two prefix sum % k the remainders are the same, then it is a valid subarray
    #     remainder_count = {} # keeps track of how many times the remainder lands on a certain number
    #     remainder_count[0] = 1
    #     subarray_count = 0
    #     sum = 0
    #     for n in nums:
    #         sum = (sum + n) % k
    #         if sum in remainder_count:
    #             subarray_count += remainder_count[sum]
    #             remainder_count[sum] += 1
    #         else:
    #             remainder_count[sum] = 1
    #     return subarray_count
    
    # use array for remainder_count instead
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # calculate prefix sum % k
        # if for any two prefix sum % k the remainders are the same, then it is a valid subarray
        remainder_count = [0 for i in range(k)] # keeps track of how many times the remainder lands on a certain number
        remainder_count[0] = 1
        subarray_count = 0
        sum = 0
        for n in nums:
            sum = (sum + n) % k
            subarray_count += remainder_count[sum]
            remainder_count[sum] += 1
        return subarray_count
    
sol = Solution()
nums = [0, 0, 0]
k = 2
print(sol.subarraysDivByK(nums, k))
