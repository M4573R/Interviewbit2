"""Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer."""

"""Analysis : With single digit elements, given the number 1,2,3,4 the largest permutation of the digits would be 4321
i.e if we reverse the digits it becomes the biggest permutation. But here's 2/more digit numbers involved so we have to
understand whether in cases like 3,43 434 or 343 would be the biggest number and sort according to that. So we compare each 
elements combination in both a+b and b+a format and sort according to that. Then we reverse the sequence and form the number.
Solution taken from leetcode.

"""



class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if(sum(A)==0):
            return "0"
        
        
        A = map(str,A)
        A.sort(cmp =lambda a,b : cmp(a+b,b+a), reverse = True)
        return str(''.join(A))
