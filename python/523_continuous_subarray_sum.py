from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # O(n) solution (with math)
        # uses prefix sum and modulo
        # probably easier to implement if i simply use a array to store all the prefixes
        if len(nums) < 2:
            return False
        sum = nums[0] % k
        modulo_vals = set()
        sum_one_step_ago = sum
        
        for i in range(1, len(nums)):
            sum = (sum + nums[i]) % k
            if sum in modulo_vals or sum == 0:
                return True
            else:
                modulo_vals.add(sum_one_step_ago)
                sum_one_step_ago = sum
        return False


    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     # O(n^2) solution (gives TLE)
    #     for i in range(len(nums) - 1):
    #         sum = nums[i]
    #         for j in range(i + 1, len(nums)):
    #             sum = sum + nums[j]
    #             if sum % k == 0:
    #                 return True
    #     return False

sol = Solution()
nums = [23,0,0]
k = 6
print(sol.checkSubarraySum(nums, k))