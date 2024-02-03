class Solution:
    def tribonacci(self, n: int) -> int:
        if n <2:
            return n
        if n ==2:
            return 1
        a,b,c = 0,1,1
        for i in range(2,n):
            ans = a+b+c
            a,b,c = b,c,ans
        return ans