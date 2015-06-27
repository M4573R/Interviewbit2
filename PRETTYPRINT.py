"""Print concentric rectangular pattern in a 2d matrix. 
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Example 2:

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 

The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array. """




class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self,A):
    #create the 2D array
        result = []
        m = 2*A - 1
        n = 2*A-1
        for i in range(m):
            result.append([0]*n)
     #set the directors of top,bottom,left and right   
        T = 0
        B = m-1
        L = 0
        R = n -1
        dir = 0
      #fill up the 2d array
        while(T<=B and L <=R):
            if(dir == 0):
                for i in xrange(L,R+1):
                    result[T][i] = A
                T+=1
                dir = 1
            elif(dir==1):
                for i in xrange(T,B+1):
                    result[i][R] = A
                R = R - 1 
                dir = 2
            elif(dir == 2):
                for i in reversed(xrange(L,R+1)):
                    result[B][i] = A
                B = B - 1
                dir = 3
            elif(dir == 3 ):
                for i in reversed(xrange(T,B+1)):
                    result[i][L] = A
                L +=1
                dir = 0
                A = A - 1
        return result


        
