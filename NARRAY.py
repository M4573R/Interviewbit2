"""You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3]

Output:[3, 4]

A = 3, B = 4."""


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        temp = [0]*len(A)
        B = list(A)
        for i in B:
            temp[i-1] += 1
                
        for i in xrange(len(temp)):
            if(temp[i]==2):
                duplicate = i + 1 
        for i in xrange(len(temp)):
            if(temp[i]==0):
                    missing = i + 1
                    
                    
        return [duplicate,missing]
