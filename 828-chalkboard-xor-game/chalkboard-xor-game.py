class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums)%2==0:
            return True
        xor = nums[0]
        for i in range(1,len(nums)):
            xor ^= nums[i] 
        if xor == 0 :
            return True
        else:
            return False