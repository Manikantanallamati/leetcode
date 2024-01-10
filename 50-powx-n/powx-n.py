class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            flag = -1
        else:
            flag = 1
        ans = 1
        n = abs(n)
        while n!=0:
            if (n%2!=0):
                n = n-1
                ans *= x
            else:
                n = n//2
                x = x*x
                # ans *= n
        if flag == -1:
            return 1/ans
        return ans