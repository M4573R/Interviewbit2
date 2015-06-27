"""Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

A -> 1

B -> 2

C -> 3

...

Z -> 26

AA -> 27

AB -> 28 """

"""Analysis : We have to map each value of the alphabet to it's respective int value where
it forms a 26-base number system. So we have to convert from 26-base to decimal number system. ord(i) - ord('A') + 1 works
to map A-Z to 1-26 by shifting values from 'A'=65. """

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        result = 0
        for i in A:
            result = result * 26 + (ord(i)-ord('A') + 1)
        return result 
