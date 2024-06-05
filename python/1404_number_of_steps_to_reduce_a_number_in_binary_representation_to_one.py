class Solution:
    def numSteps(self, s: str) -> int:
        if s == "1":
            return 0
        if s[-1] == "1":
            # add one
            s = self.add_one_helper(s)
            return 1 + self.numSteps(s)
        else:
            # divide by two
            s = self.divide_by_two_helper(s)
            return 1 + self.numSteps(s)
    
    def add_one_helper(self, s):
        if s[0] == "1":
            s = "0" + s
        carry = 1
        ls = list(s)
        for i in range(len(s) - 1, -1, -1):
            if carry == 0:
                break
            if ls[i] == "1":
                ls[i] = "0"
            else:
                ls[i] = "1"
                carry = 0
        s = ''.join(ls)
        return s if s[0] != "0" else s[1:]

    def divide_by_two_helper(self, s):
        return s[:-1]
    
sol = Solution()
p = sol.numSteps("1000001")
print(p)