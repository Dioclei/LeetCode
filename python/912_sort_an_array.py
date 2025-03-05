from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # implement merge sort
        # recursively merge two sorted arrays
        if len(nums) <= 1:
            return nums
        else:
            mid = len(nums) // 2
            arr1 = self.sortArray(nums[:mid])
            arr2 = self.sortArray(nums[mid:])
            return self.merge(arr1, arr2)

    def merge(self, arr1, arr2):
        # merge two sorted arrays together
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(arr1) or p2 < len(arr2):
            if p1 == len(arr1):
                # append the rest of arr2
                result.append(arr2[p2])
                p2 += 1
            elif p2 == len(arr2):
                # append the rest of arr1
                result.append(arr1[p1])
                p1 += 1
            else:
                # do a comparison and append the smallest number
                if arr1[p1] <= arr2[p2]:
                    result.append(arr1[p1])
                    p1 += 1
                else:
                    result.append(arr2[p2])
                    p2 += 1
        return result
        