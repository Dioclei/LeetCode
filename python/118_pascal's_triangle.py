from typing import List

# Problem: generate a Pascal's triangle with the given number of rows
# Intuition
# - in Pascal's triangle, each number is the sum of the 2 numbers above it
# - generate row by row, using the previous row to calculate the next row
# Comments
# - using a previous step to generate the next step is also known as dynamic programming (DP)
# - the main difficulties with DP lie in identifying the DP pattern and which parts of the data are involved in the DP,
# - and creating an appropriate data structure to store the DP data.
# - this DP problem is relatively simple as it simply uses a 2d array to store the data, and the problem even tells you to create a 2d array.

class Solution:
    def generateHelper(self, previousRow):
        result = []
        result.append(1) # the row always starts and ends with 1
        # compute the middle values with previousRow values
        p = 1
        while p < len(previousRow):
            val = previousRow[p-1] + previousRow[p]
            result.append(val)
            p += 1
        result.append(1) # the row always starts and ends with 1
        return result
    
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                prev = result[i-1]
                result.append(self.generateHelper(prev))
        return result

s = Solution()
print(s.generate(5))