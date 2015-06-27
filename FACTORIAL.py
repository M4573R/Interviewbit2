
"""Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

source : http://www.programmerinterview.com/index.php/java-questions/find-trailing-zeros-in-factorial/

"""


class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        if(A == 5):
            return 1
        j = 5
        while(A/j>=1):
            count+=A/j
            j*=5
        return count


























