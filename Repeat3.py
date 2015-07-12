"""You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times.

reference : http://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python """

from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        B= Counter(A).most_common()
        for i in xrange(len(B)):
            if(B[i][1] > len(A)/3):
                result = B[i][0]
                return result
        return -1
