# Problem: given a method read4 that reads from a file at 4 characters per read, read n characters and output actual number of characters read
# Intuition:
# - calculate number of times to call read4
# - read4 will output number of characters read so simply total it up

# Comments
# - the reason that this problem was posed is that it teaches concepts of systems programming - reading 4 bytes at once is faster than 1 byte at a time
# - we then need to resolve: 
#   - what if we read more than we need? i.e. total read > n
#   - what if read4 returns eof, indicating that there is no more to read? i.e. total read < n
# - easiest way to implement this is to use an internal buffer of 4 characters
# - speedup by implementing a pointer directly to destination buffer, removing the need for the internal buffer

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        num_read4_calls = (n - 1) // 4 + 1
        buf4 = [""] * 4 # input buffer
        total_chars_read = 0
        i = 0
        while i < num_read4_calls:
            # 1. read into intermediate buffer buf4
            num_chars_read = read4(buf4)
            j = 0
            while j < num_chars_read and total_chars_read < n:
                # 2. read from intermediate buffer buf4 into destination buffer buf
                buf.append(buf4[j])
                j += 1 
                total_chars_read += 1
            i += 1
        return total_chars_read