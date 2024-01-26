def Ugly(n):
    if n==2 or n==3 or n==5:
        return True
    if n%5==0:
        return Ugly(n//5)
    elif n%3==0:
        return Ugly(n//3)
    elif n%2==0:
        return Ugly(n//2)
    else:
        return False
class Solution:
    def isUgly(self, n: int) -> bool:    
        if n==1:
            return True
        if n==0:
            return False
        return Ugly(n)