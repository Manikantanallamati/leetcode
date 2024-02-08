class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        i = 2
        ans = 9
        x = 9
        res = 10

        while i<=n:

            ans = ans * (x)
            x -= 1
            res += ans
            i += 1
        return res


        