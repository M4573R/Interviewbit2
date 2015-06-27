class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
         
            
        m = len(A)
        n = len(A[0])
        T = 0
        B = m-1
        L = 0
        R = n -1
        dir = 0
        if(len(A[0])==1 and len(A)==1):
                result.append(A[0][0])
                return result
        
        while(T<=B and L <=R):
             
            if(dir == 0):
                for i in xrange(L,R+1):
                    result.append(A[T][i])
                T+=1
                dir = 1
            elif(dir == 1 ):
                for i in xrange(T,B+1):
                    result.append(A[i][R])
                R = R - 1 
                dir = 2
            elif (dir ==2):
                for i in reversed(xrange(L,R+1)):
                    result.append(A[B][i])
                B = B - 1
                dir = 3
            elif(dir == 3 ):
                for i in reversed(xrange(T,B+1)):
                    result.append(A[i][L])
                L += 1
                dir = 0
        return result
