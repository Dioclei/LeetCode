# String problem
# Searching for an occurrence in a string
# Intuition
# - 2-pointer brute force search, but is there a better method?

# Comments
# - the implemented solution is known as a sliding window. 
# - i.e. you keep a startWindow pointer (haystack pointer) and iterate through the window (needle pointer)
# - it can be optimised by reducing the number of times the window is iterated
# Rabin-Karp Algorithm
# - using hashing, we can keep a hash of the needle, and check if the corresponding substring in the haystack has an equal hash
# - only iterate through the window when the hashes are equal, to make sure the matched substring is correct.
# - further optimisations: rolling hash, use 2 hashes

# my solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0 # haystack pointer
        p2 = 0 # needle pointer
        while p1 < len(haystack) - len(needle) + 1: # deduct length of needle to not go out of range
            while p2 < len(needle):
                if haystack[p1+p2] == needle[p2]:
                    # correct character, check next character
                    p2 += 1
                else:
                    # incorrect character, break and find next match
                    p2 = 0
                    break
            # end loop if needle is found
            if p2 == len(needle):
                return p1
            p1 += 1
        return -1

# Rabin-Karp Algorithm implementation, with a rolling, single hash
# I keep the hash algorithm simple here but of course it could be more complicated to reduce spurious hits (false positives)
class Solution:
    # hash algorithm: take the ord value of each character and add it togther
    def strHash(self, substring):
        val = 0
        for c in substring:
            val += ord(c)
        return val

    # checks if s1 is equal to s2
    def isMatch(self, s1, s2):
        if len(s1) != len(s2):
            raise ValueError("Only equal length strings allowed to match")
        p = 0
        while p < len(s1):
            if s1[p] != s2[p]:
                return False
            p += 1
        return True

    def strStr(self, haystack: str, needle: str) -> int:
        needleHash = self.strHash(needle)
        p = 0
        while p < len(haystack) - len(needle) + 1:
            if p == 0:
                # compute first hash
                currentHash = self.strHash(haystack[:len(needle)])
            else:
                # update hash
                currentHash -= self.strHash(haystack[p-1])
                currentHash += self.strHash(haystack[p+len(needle)-1])
            if currentHash == needleHash:
                # check if the values match
                if self.isMatch(haystack[p:p+len(needle)], needle):
                    return p            
            # increment pointer
            p += 1
        return -1
    
                