# easy

class Solution(object):

    # O(n + m) two pointer solution
    def getCommonTwoPointer(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        # nums1 and nums2 are already sorted in non-decreasing order, 
        # so we just need to use two pointers to find the minimum

        p1 = 0
        p2 = 0
        len1 = len(nums1)
        len2 = len(nums2)

        while p1 < len1 and p2 < len2:
            e1 = nums1[p1]
            e2 = nums2[p2]
            if e1 == e2:
                return e1
            elif e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return -1
    
    # O(nlogm) binary search solution 
    def binary_search(self, num, l):
        min = 0
        max = len(l) - 1
        mid = (min + max) // 2
        while min < max:
            if num == l[mid]:
                return num
            if num < l[mid]:
                max = mid - 1
                mid = (min + max) // 2
            else:
                min = mid + 1
                mid = (min + max) // 2
        # min == max
        return num if l[min] == num else -1
            
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        for x in nums1:
            v = self.binary_search(x, nums2)
            if v != -1:
                return v
        return -1

