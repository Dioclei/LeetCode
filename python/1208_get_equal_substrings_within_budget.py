class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # a substring is a contiguous sequence of characters within a string
        # sliding window O(n) solution, but it's not as good as the editorial,
        # the actual time taken is slower because there's too many if statements

        # p1 = 0
        # p2 = 0
        # cost = 0
        # current_length = 0
        # max_length = 0
        # while p2 < len(s):
        #     # attempt to add more letters
        #     new_cost = self.get_cost(s, t, p2)
        #     if cost + new_cost <= maxCost:
        #         p2 += 1
        #         current_length += 1
        #         max_length = max(max_length, current_length)
        #         cost += new_cost
        #     elif p1 == p2:
        #         # no letters currently selected,
        #         # increment both p1 and p2 to find a substring that starts later
        #         p1 += 1
        #         p2 += 1
        #         continue
        #     else:
        #         # some letters currently selected
        #         # increment p1 to reduce cost so that i can increment p2
        #         cost -= self.get_cost(s, t, p1)
        #         p1 += 1
        #         current_length -= 1
        # return max_length
    
        # slightly faster but not that much faster tbh
        # but this is the proper sliding window method
        p1 = 0
        p2 = 0
        current_cost = 0
        max_length = 0
        for i in range(len(s)):
            # keep adding from the right
            current_cost += self.get_cost(s, t, p2)
            p2 += 1

            # if selected substring is invalid, reduce from the left
            while current_cost > maxCost:
                current_cost -= self.get_cost(s, t, p1)
                p1 += 1

            # if selected substring is valid, do the necessary calculations
            length = p2 - p1
            max_length = max(max_length, length)
        return max_length
            


                    
    def get_cost(self, s, t, index):
        return abs(ord(s[index]) - ord(t[index]))
    
    

sol = Solution()
p = sol.equalSubstring("abcd", "acde", 0)
print(p)