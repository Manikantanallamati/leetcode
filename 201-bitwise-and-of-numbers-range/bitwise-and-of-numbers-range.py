class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left << 1 < right:
            return 0


        while right > left:
            right = right & (right - 1)
            
        return right & left
        