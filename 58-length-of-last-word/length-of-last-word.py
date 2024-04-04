class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        length = 0
        for i in s:
            length = len(i)
        return length