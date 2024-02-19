class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if n<0:
            return False
        for i in range(31,-1,-1):
            mask = 1 << i
            if mask & n>0:
                count +=1
        if count == 1:
            return True
        else:
            return False