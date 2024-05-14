# medium
# did this in java already but trying to see if i can come up with a solution again, 
# but in python (and without looking at my prev ans)

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s + "$"

        # sliding window
        start_p = 0
        end_p = 0
        current_c = s[0]
        current_characters = set()
        current_characters.add(current_c)
        current_characters_count = 0
        max_count = 0

        while end_p < len(s):
            print(current_characters)
            # find how long current_c is
            c = s[end_p]
            if not c == current_c:
                # new character
                # tabulate old character
                current_c_count = end_p - start_p
                current_characters_count += current_c_count
                max_count = max(max_count, current_characters_count)

                # check if new character is in current_characters
                current_c = c
                if len(current_characters) < 2:
                    current_characters.add(current_c)
                elif not current_c in current_characters:
                    # remove oldest character and add in new character
                    old_c = s[start_p - 1]
                    current_characters.remove(old_c)
                    current_characters.add(current_c)
                    current_characters_count = current_c_count

                # prepare to count next character
                start_p = end_p

            end_p += 1
        return max_count





    # def lengthOfLongestSubstringTwoDistinct(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """

    #     # two queue solution
        
    #     character_queue = [None, None]
    #     count_queue = [0, 0]
    #     current_character_count = 0
    #     max_count = 0

    #     for i in range(len(s)):
    #         print(count_queue)
    #         c = s[i]
    #         if c == character_queue[-1]:
    #             count_queue[-1] += 1
    #             current_character_count += 1
    #             max_count = max(max_count, current_character_count)
    #         else:
    #             character_queue.append(c)
    #             count_queue.append(1)
    #             removed_c = character_queue.pop(0)
    #             count_queue.pop(0)
    #             if c == removed_c:
    #                 # still old word
    #                 current_character_count += 1
    #                 max_count = max(max_count, current_character_count)
    #             else:
    #                 # count new word
    #                 current_character_count = sum(count_queue)
    #                 max_count = max(max_count, current_character_count)
    #     return max_count

def test():
    s = Solution()
    count = s.lengthOfLongestSubstringTwoDistinct("aaabbccccd")
    print(count)

test()
                
            
            
