# medium

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        

        if k == len(num):
            return "0"

        # maintain that the first m characters are monotonically increasing, for some m

        num = list(num)
        new_num = []

        # append while k > 0, making sure new_num is monotonically increasing

        new_num.append(num[0])
        i = 1
        while i < len(num):
            next = num[i]
            if k > 0:
                # compare with top of stack
                if len(new_num) == 0:
                    new_num.append(next)
                    i += 1
                elif next < new_num[-1]:
                    # remove the top of the stack and re-loop
                    new_num.pop()
                    k -= 1
                else:
                    # add to stack
                    new_num.append(next)
                    i += 1
            else:
                # add to stack
                new_num.append(next)
                i += 1
        # number is monotonically increasing but we still need to remove more digits, do a slice
        if k > 0:
            new_num = new_num[:-k]
        
        # remove leading zeros
        while len(new_num) > 1 and new_num[0] == '0':
            new_num.pop(0)
        return "".join(new_num)

def test():
    s = Solution()
    a = s.removeKdigits("10001", 4)
    print(a)

test()