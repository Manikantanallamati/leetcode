class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        less = 0
        high = len(s)-1
        s = list(s)
        while less<high:
            if s[less] not in vowels:
                less+=1
            if s[high] not in vowels:
                high -=1
            if s[high] in vowels and s[less] in vowels:
                s[high],s[less] = s[less],s[high]
                less+=1
                high -=1
        return "".join(s)
