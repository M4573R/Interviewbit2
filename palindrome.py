""" Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

For example, 
12121 is a palindrome number.
123 is not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem """

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):      
        return int(str(A)==str(A)[::-1])
        
        
        
#Second solution

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if(A<0):
            return 0
        if(A in [1,2,3,4,5,6,7,8,9]):
            return 1
        reversed = int(str(A)[::-1])
        if(reversed == A):
            return 1
        else:
            return 0
