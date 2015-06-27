"""Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer"""

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
    #INTMAX = 2^31-1 for 32 bit signed integer
        max =  2147483647
        
        if(A<0):
            minus = -1*A
            minus = str(minus)[::-1]
            result = int("-" + minus)
            if(result > max or result < -max):
                return 0
            else:
                return result
        else:
            result = int(str(A)[::-1])
            if(result > max or result <= -max):
                return 0
            else:
                return result
            
            
        
