class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 1 or n == 3:
            return n
        b = 2
        a = 3
        for i in range(4,n+1):
            val = a+b
            b = a
            a = val
        return val