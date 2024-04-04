class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        length = 0
        length = len(s[len(s)-1])
        return length