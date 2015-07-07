
"""Given an m x n matrix, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1

On returning, the array A should be :

0 0 0
1 0 1
1 0 1
Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity. """


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        row = [0]*len(A)
        column = [0]*len(A[0])
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if(A[i][j]==0):
                    row[i]=True
                    column[j]=True
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if(row[i] == True or column[j] == True):
                    A[i][j] = 0
        return A
        
        
"""Space efficient solution :

We are going to use the first row and the first column of the 2d list
to store information about the rest of the columns and rows to save
space. First we will check if the first row or the first column
has any zeroes and save it in a boolean variable. Then we will search
through the rest of the list and set corresponding rows and columns to
zero/true. Each column i in first row stores information about whether that
column has any zero in the ith column, and each row in the first column
stores information whether there's any zero in the row i."""



class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        
        hasrowzero = False
        hascolzero = False
    # Does the first row has any zero?
        for j in xrange(n):
            if(A[0][j] == 0):
                hasrowzero = True
    # Does the first column has any zero?
                
        for i in xrange(m):
            if(A[i][0] == 0):
                hascolzero = True
    # Set true to the columns and rows of the first row and column    
        for i in xrange(1,len(A)):
                for j in xrange(1,len(A[0])):
                    if(A[i][j]==0):
                        A[0][j]=0
                        A[i][0] = 0
    #Set the correct entries to zero                    
        for i in xrange(1,len(A)):
                for j in xrange(1,len(A[0])):
                    if(A[i][0] == 0 or A[0][j] == 0):
                        A[i][j] = 0
                        
    #Does the first row need to get updated?
        if(hasrowzero==True):
            for j in xrange(n):
                A[0][j] = 0
    #Does the first column need to be updated?
                
        if(hascolzero==True):
            for i in xrange(m):
                A[i][0] = 0
                
        return A

        
