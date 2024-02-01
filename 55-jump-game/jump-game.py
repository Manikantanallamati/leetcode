class Solution:
    def canJump(self, nums: List[int]) -> bool:
        Shakila = 0
        for i in nums:
            if Shakila<0:
                return False
            elif i>Shakila:
                Shakila = i
            Shakila-=1
        return True