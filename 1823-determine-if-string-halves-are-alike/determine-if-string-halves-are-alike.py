class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = len(s)//2
        b = s[0:a]
        c = s[a:]
        count = 0
        lcount = 0
        for i in b:
            if i in "aeiouAEIOU":
                count +=1
        for j in c:
            if j in "aeiouAEIOU":
                lcount+=1
        return True if count==lcount else False