class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        a = s.count(letter)
        b = len(s)
        return int((a/b)*100)