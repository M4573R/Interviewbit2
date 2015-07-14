"""Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.

You may also assume that the difference will not overflow."""

#Solution 1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if(len(A)<2):
            return 0
        if(len(A)==2):
            return max(A)-min(A)
        A = sorted(A)
        result = []
        for i in xrange(len(A)-1):
            result.append(A[i+1] - A[i])
        return max(result)
