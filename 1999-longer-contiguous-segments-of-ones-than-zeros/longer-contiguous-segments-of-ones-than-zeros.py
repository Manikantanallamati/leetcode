class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        lcount = 0
        count = 0
        # a = []
        # b = []
        y = 0
        z = 0
        for i in s:
            if i =='1':
                count +=1
                # a.append(count)
                lcount = 0
                y = max(y,count)
            else:
                count = 0
                lcount+=1
                # b.append(lcount)
                z = max(z,lcount)
        if y == z:
            return False
        if y>z:
            return True
        else:
            return False    