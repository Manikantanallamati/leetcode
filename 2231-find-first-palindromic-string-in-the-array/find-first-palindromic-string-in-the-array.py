class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            b = i[::-1]
            if i==b:
                return i
                break
        else:
            return ("")
