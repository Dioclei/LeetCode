# list traversal problem
# Intuition
# - brute force add one to the last digit, and recursively add one to the previous digits if it goes 9 -> 10
# - brute force may cause the list to grow in length
# - is there a better solution?

# Comments
# - there's not really a better solution other than the simply adding.
# - however there's no need for the add_one variable or modulo, as the moment u reach a non-nine the loop should break.
# - a simple problem but it changes slightly based on the data structure given. this is probably the simplest version.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # brute force add from the last digit
        add_one = True
        for i in range(len(digits)-1, -1, -1):
            if add_one:
                new_val = digits[i] + 1
                digits[i] = new_val % 10
                if new_val != 10:
                    add_one = False
            else:
                break
        if add_one:
            digits = [1] + digits
        return digits