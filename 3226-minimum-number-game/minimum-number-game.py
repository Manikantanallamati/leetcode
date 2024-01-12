class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return 0
        b = []
        for i in range(len(nums)//2):
            alice = min(nums)
            nums.remove(min(nums))
            bob = min(nums)
            nums.remove(min(nums))
            b.append(bob)
            b.append(alice)
        return b