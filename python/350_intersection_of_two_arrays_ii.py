from typing import List

class Solution:
    # hashmap solution has better time complexity
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)
        h = {}
        for n in nums1:
            if n in h:
                h[n] += 1
            else:
                h[n] = 1
        intersection = []
        for m in nums2:
            if m in h and h[m] > 0:
                intersection.append(m)
                h[m] -= 1
        return intersection

    # sorting solution
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        intersection = []
        while p1 < len(nums1) and p2 < len(nums2):
            n1 = nums1[p1]
            n2 = nums2[p2]
            if n1 < n2:
                p1 += 1
            elif n1 > n2:
                p2 += 1
            else:
                intersection.append(n1)
                p1 += 1
                p2 += 1
        return intersection
        
            