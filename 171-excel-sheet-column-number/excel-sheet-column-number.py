class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a = 0
        # value = ord('B')-64
        # return 0
        if len(columnTitle)==1:
            return ord(columnTitle)-64
        for i in range(len(columnTitle)):
            if i==0:
                a+=(ord(columnTitle[-i-1])-64)
            else:
                a+=(ord(columnTitle[-i-1])-64)*(26**i)
        return a