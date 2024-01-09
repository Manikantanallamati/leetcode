class Solution:
    def bulbSwitch(self, n: int) -> int:
        # a = [1]*n
        # if n ==1 or n == 0:
        #     return n
        # if n == 2:
        #     return 1
        # for i in range(2,n):
        #     for j in range(0,n):
        #         if j%i == 0 and a[j] == 0:
        #             a[j] = 1
        #         elif j%i == 0 and a[j] == 1:
        #             a[j] = 0
        # return a.count(1)
        return int(math.sqrt(n))