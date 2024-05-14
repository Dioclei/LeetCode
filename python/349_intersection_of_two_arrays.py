# easy

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        intersection = {}
        while p1 < len(nums1) and p2 < len(nums2):
            a = nums1[p1]
            b = nums2[p2]
            if a == b:
                intersection[a] = True
                p1 += 1
                p2 += 1
            elif a < b:
                p1 += 1
            else:
                p2 += 1

        return list(intersection)