# http://www.interviewbit.com/courses/programming/topics/math/problems/paths/


import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        def nCr(n,r):
            f = math.factorial
            return f(n) / f(r) / f(n-r)
        return nCr(A+B-2,A-1)
