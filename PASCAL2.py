"""Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given k = 3,

Return [1,3,3,1].

NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?"""

#Approach 1 : Generate Pascal's triangle, return the ith row

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        def generate(A):
            result = []
            if(A==0):
                return result
            elif(A==1):
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
            
        result = generate(A+1)
        return result[A]
