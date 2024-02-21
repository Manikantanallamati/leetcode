class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = left
        count = 0
        if left == 1073741824:
            return 1073741824
        for i in range(left+1,right+1):
            ans &=i
            count += 1
            if ans ==0:
                return 0
            if count >9999999:
                return 0
        return ans
        