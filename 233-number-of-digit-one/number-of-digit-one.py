# import sys
# sys.setrecursionlimit(1000000000)
class Solution:
    def countDigitOne(self, n: int) -> int:
        # def One(n,cnt):
        #     if int(n) ==0:
        #         return cnt
        #     cnt+=str(n).count('1')
        #     return One(n-1,cnt)
        # cnt = 0
        # return One(n,cnt)
        count = 0
        digit = 1
        while digit <= n:
            divider = digit * 10
            count += (n // divider) * digit + min(max(n % divider - digit + 1, 0), digit)
            digit *= 10
        return count
