"""Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Given n = 3,

You should return the following matrix:
 [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ] """





class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, A):
        
        if A<=0:
            return [] 
 
        # Generate a A X A matrix to store the numbers
        
        result = []
        m = A
        n = A
        for i in range(m):
            result.append([0]*n)
        
        
     #set the directors of top,bottom,left and right   
        T = 0
        B = m-1
        L = 0
        R = n -1
        dir = 0
        cur = 1
      #fill up the 2d array until current > A*A
        while(True):
            if(cur > A*A):
                break
            if(dir == 0):
                for i in xrange(L,R+1):
                    result[T][i] = cur
                    cur+=1
                T+=1
                dir = 1
            elif(dir==1):
                for i in xrange(T,B+1):
                    result[i][R] = cur
                    cur+=1
                R = R - 1 
                dir = 2
            elif(dir == 2):
                for i in reversed(xrange(L,R+1)):
                    result[B][i] = cur
                    cur+=1
                B = B - 1
                dir = 3
            elif(dir == 3 ):
                for i in reversed(xrange(T,B+1)):
                    result[i][L] = cur
                    cur+=1
                L +=1
                dir = 0
                
        return result
