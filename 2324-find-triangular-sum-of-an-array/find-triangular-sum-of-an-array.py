class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                nums[j]=int(str(nums[j]+nums[j+1])[-1])
                # print(nums[j])
            a = nums.pop()
        return a