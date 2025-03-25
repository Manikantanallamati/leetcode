class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        if str1[0] == '-':
            return(False)
        else:
            return(True if int(str1[::-1])==int(str1) else False)