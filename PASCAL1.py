"""Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return
 [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ] """

"""Analysis : 1. The first and last element in each row is 1
              2. The other elements are the sum of the two elements in the previous row which are right above it.
              3. So we add 1 to the first and last element of each row and for other elements we sum the appropriate
              two elements in the previous row """


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        result = []
        if(A==0):
            return result
        if(A==1):
            return [[1]]

        elif(A==2):
            result.append([1])
            result.append([1,1])
            return result
        else:    
            result.append([1])
            result.append([1,1])
            # create the rows and set the first and last element of the row to one
            for i in xrange(3,A+1):
                newrow = [0]*i
                newrow[0] = 1
                newrow[i-1] = 1
                result.append(newrow)
            # for each row from 2 to the last one we set the elements from 1 to the one before last
            #(excluding first and last) the sum of the upper rows elements
            for i in xrange(2,A):
                for j in xrange(1,i):
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
            return result
