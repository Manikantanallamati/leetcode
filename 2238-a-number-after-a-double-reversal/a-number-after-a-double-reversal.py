class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = int(str(num)[::-1])
        b = int(str(a)[::-1])
        if num == int(b):
            return True
        else:
            return False