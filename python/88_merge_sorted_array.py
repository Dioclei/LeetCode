from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from the back
        p1 = m - 1
        p2 = n - 1
        p3 = len(nums1) - 1 # back of the list
        while p3 > -1:
            if p1 == -1:
                nums1[p3] = nums2[p2]
                p2 = p2 - 1
            elif p2 == -1 or nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 = p1 - 1
            else:
                nums1[p3] = nums2[p2]
                p2 = p2 - 1
            p3 = p3 - 1

sol = Solution()
n1 = [2, 0]
n2 = [1]
sol.merge(n1, 1, n2, 1)
print(n1)