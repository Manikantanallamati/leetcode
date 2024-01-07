class Solution:
    def countPrimes(self, n: int) -> int:
        N = n
        primes = [True for i in range(N+1)]
        p = 2
        while p*p<=N+1:
            if primes[p] == True:
                for i in range(p*p,N+1,p):
                    primes[i] = False
            p += 1
        k = 2
        c=0
        for p in range(2,N):
            # print(primes[p])
            if primes[p]:
                c+=1
        return c