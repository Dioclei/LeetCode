# easy

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # naive solution
        num_count = [0] * 101
        for x in nums:
            num_count[x] += 1
        max_count = 0
        max_count_count = 0
        for i in range(1, len(num_count)):
            if num_count[i] > max_count:
                max_count = num_count[i]
                max_count_count = 1
            elif num_count[i] == max_count:
                max_count_count += 1
        return max_count_count * max_count

        # possible to do in one pass by keeping a table of frequencies

    def test(self, input):
        print(self.maxFrequencyElements(input))

s = Solution()
s.test([1,2,3,4,5])
