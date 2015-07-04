"""Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.

"""



class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        if(len(A)==0):
            return 1
        for i in range(0, len(A)):
            j = i
            while A[j] > 0 and A[j] <= len(A) and  A[j] != A[A[j] - 1]:
                t = A[j] - 1
                A[j], A[t] = A[t], A[j]

        for i in range(0, len(A)):
            if A[i] != i + 1:
                return i + 1

        return len(A) + 1
