from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # count occurences of each value
        count = {}
        for v in arr1:
            if v in count:
                count[v] += 1
            else:
                count[v] = 1
        result = [None] * len(arr1)
        p = 0
        for c in arr2:
            repeat = count.pop(c) # remove the value from count
            for i in range(repeat):
                result[p] = c
                p += 1
        for c in sorted(count.keys()):
            repeat = count.pop(c)
            for i in range(repeat):
                result[p] = c
                p += 1
        return result

    
sol = Solution()
arr1 = [1, 2, 3, 3, 6, 3, 4, 5]
arr2 = [5, 4, 2, 1, 3]
res = sol.relativeSortArray(arr1, arr2)
print(res)
        
