# medium

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        p1 = 0
        p2 = 0
        c = None
        count = 0
        while p1 < len(chars):
            v = chars[p1]
            if v != c:
                # write count for prev character
                if count > 1:
                    count_str = str(count)
                    for x in count_str:
                        chars[p2] = x
                        p2 += 1
                # write new character
                c = v
                # write to chars and re-initialise count
                count = 1
                chars[p2] = c
                p1 += 1
                p2 += 1
            else:
                # count number of characters
                count += 1
                p1 += 1
        # write for last character
        if count > 1:
            count_str = str(count)
            for x in count_str:
                chars[p2] = x
                p2 += 1
        return p2

