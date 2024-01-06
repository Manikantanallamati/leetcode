class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for i in range(len(s)):
            if s[i].isalnum():
                a+=s[i]
        a=a.lower()
        print(a)
        if a==a[::-1] or s==' ':
            return True
        else:
            return False