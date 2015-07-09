You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]

#Solution 1 :

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        if(len(A)==1):
            return A
        #Transpose the matrix    
        A = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
        #reverse the rows
        for c in A:
            c.reverse()
        return A
        
#Solution 2 :

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
    #Creates the transpose and reverses the rows.
    #Example : [[1,2,3],[4,5,6],[7,8,9]] becomes [[1,4,7],[2,5,8],[3,6,9]] with zip applied and we just reverse it
        return zip(*A[::-1])


#Solution 3:

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        if(len(A)==1):
            return A
    #We explore the matrix in layers. There are i = len(A)/2 layers.        
        for i in xrange(len(A)/2):
            j = i
    # for each layer we shift 4 elements in a directed cycle of top_left-->top_right-->bottom_right--->bottom_left. 
    # See hints for further explanation.        
            while(j < len(A) - i - 1 ):
                temp = A[i][j]
                A[i][j] = A[len(A)-j-1][i]
                A[len(A)-j-1][i] = A[len(A)-i-1][len(A)-j-1]
                A[len(A)-i-1][len(A)-j-1] = A[j][len(A)-i-1]
                A[j][len(A)-i-1] = temp
                j+=1
        return A
