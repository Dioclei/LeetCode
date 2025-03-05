# A palindrome is a sequence that is the same when read from the left and from the right
# My intuition is to convert the given integer into a string and use a two-pointer algorithm to check from left and right

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        p1 = 0
        p2 = len(strX) - 1
        while (p1 < p2):
            if strX[p1] == strX[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True

# Can it be done without converting the integer to string?
# Simply reverse the number by slowly iterating through from the ones place and checking if the numbers are the same
