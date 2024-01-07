class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        c = 0
        for i in range(31,-1,-1):
            if (n>>c)&1:
                ans += 2**i
            c+=1
        return ans