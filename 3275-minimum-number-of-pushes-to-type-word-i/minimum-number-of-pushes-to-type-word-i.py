class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        b = len(word)
        i = 1
        while b>8:
            ans+=8*i
            b = b-8
            i+=1
        ans +=b*i
        return ans