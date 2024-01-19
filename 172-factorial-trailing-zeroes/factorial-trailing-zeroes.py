class Solution:
    def trailingZeroes(self, n: int) -> int:
        m = 0
        s = 5
        while n>=s:
            m+=n//s
            s = s*5
        # return n//5+n//25+n//125+n//625+n//3125+n//15625+n//78125+n//390625
        return m