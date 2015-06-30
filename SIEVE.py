"""Given a number N, find all prime numbers upto N ( N included ).

Example:

if N = 7,

all primes till 7 = {2, 3, 5, 7}

Make sure the returned array is sorted."""


class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        primes =[1]*(A+1)
        for i in xrange(A+1):
            primes[i] = 1
        primes[0] = 0
        primes[1] = 0
        for i in xrange(2,int(math.sqrt(A))+1):
            if(primes[i] == 1):
                j =2 
                while(i*j <=A):
                    primes[i*j]= 0
                    j+=1
        result = []
        for index, value in enumerate(primes):
            if(value == 1):
                result.append(index)
        result.sort()
        return result
