class Solution:
    def convertToBase7(self, num: int) -> str:
        val = num
        if num==0:
            return "0"
        if num<0:
            num *= -1
        a = []
        while num>0:
            a.append(str(num%7))
            num = num//7
        ans = a[::-1]
        if val<0:
            ans = "-"+str("".join(ans))
            return str(ans)
        else:
            return "".join(ans)