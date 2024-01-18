class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        b = ""
        num = s[::-1]
        s.clear()
        s+=num