def Happy(n):
    if n==1:
        return True
    if n==4:
        return False
    else:
        val = 0
        for i in str(n):
            val += int(i)**2 
        return Happy(val)
class Solution:
    def isHappy(self, n: int) -> bool:
        return Happy(n)