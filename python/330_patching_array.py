from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # nums_ptr points to the earliest number in nums that is not in the sum calculation
        nums_ptr = 0
        # sum that we need to achieve
        # maintain invariant: all sums < target_sum are currently achievable
        target_sum = 1
        # number of patches needed
        patches = 0

        # important optimisation:
        # rather than checking all sums < n, we know that:
        # 1. all sums < target_sum are achievable
        # 2. by patching in any number k, all sums < target_sum + k are now achievable, because we can add k to any previously achievable sum.
        # 3. therefore, we simply increment target_sum appropriately, and don't need to check every sum

        while target_sum <= n:
            # patch a new number to obtain target_sum
            # either:
            # 1. take a new number from nums, if the new number is smaller
            if nums_ptr < len(nums) and nums[nums_ptr] <= target_sum:
                new_number = nums[nums_ptr]
                # increment nums_ptr for the next number
                nums_ptr += 1
            # 2. patch in target_sum, note that there is no need to patch in earlier numbers, because the invariant is that all previous numbers are obtainable.
            else:
                new_number = target_sum
                patches += 1
            # increment target_sum
            target_sum = target_sum + new_number
        
        return patches
    
    
sol = Solution()
# print(sol.count_until(2147483647))
print(sol.minPatches([1,2,31,33], 2147483647))

        
            
