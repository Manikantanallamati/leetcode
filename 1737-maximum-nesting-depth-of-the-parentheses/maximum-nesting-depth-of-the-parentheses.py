class Solution:
    def maxDepth(self, s: str) -> int:
        open = 0
        close = 0
        a = []
        for i in s:
            if i == '(':
                open+=1
                a.append(open)
            elif i == ')':
                close+=1
                a.append(close)
                open-=1    
                close -= 1
        # print(a)
        if len(a) <= 1:
            return 0
        return max(a)