class Solution:
    def arrangeCoins(self, n: int) -> int:
        # i = 0
        # a = n
        # count = 0
        # while n>0:
        #     i += 1
        #     n = n-i
        #     count = 0
        #     count+=i
        # if count == 0:
        #     return count
        # elif count == 1:
        #     return count 
        # elif a == 3:
        #     return 2
        # else:
        #     return count-1
        val = n
        for i in range(1,n+1):
            val -= i
            if val<0:
                return i-1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1