"""Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
"""

""" Approach : We traverse the string from the end. When the first word begins Flag is set to True. 
If we encounter a whitespace and if Flag was true before it means the first word from the end i.e last word just ended so flag
is still true. If there's no whitespace in string, we return the length of string """ 
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if(A ==''):
            return 0
        if(len(A)==1):
            return 1
        flag = False
        count = 0
        
        for i in xrange(len(A)-1,-1,-1):
            if(A[i]!=' '):
                flag = True
                count = count + 1
            else : 
                if(flag):
                    return count
        return count
