class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """

        # TLE O(n^2)
        count = 0
        for i in range(len(word)):
            count_polarity = [False for z in range(10)]
            odd_count = 0
            for j in range(i, len(word)):
                # giga fast O(1)
                c = word[j]
                index = ord(c) - 97
                if count_polarity[index]:
                    odd_count -= 1
                else:
                    odd_count += 1
                count_polarity[index] = not count_polarity[index]
                if odd_count <= 1:
                    count += 1
        return count
    
s = Solution()
print(s.wonderfulSubstrings("aabb"))