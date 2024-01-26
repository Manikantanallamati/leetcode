def Digits(val,k):
    if k==1:
        return val
    else:
        k-=1
        z = 0
        for i in str(val):
            z += int(i)
        val = z 
        return Digits(val,k)
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = ''
        val = 0
        for i in s:
            a+=str((ord(i)-96))
        for i in a:
            val +=int(i)
        return Digits(val,k)