class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0:
            return -1
        val = 1
        for i in range(k):
            if val % k == 0:
                return i+1
            val = (val*10)+1
        return -1 