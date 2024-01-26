class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time <n:
            return time+1
        else:
            a = time//(n-1)
            if a%2==0:
                return 1+time%(n-1)
            else:
                return n-time%(n-1)
