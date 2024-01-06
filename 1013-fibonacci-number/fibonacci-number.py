class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(1,n+1):
            val = a+b
            a = b
            b = val
        return a