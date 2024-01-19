class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s=1
        c=0
        n=[0]*len(nums)
        for i in  nums:
            if i != 0 :
                s*=i
        if nums.count(0)==len(nums):
            return nums
        if nums.count(0)>1:
            return n
        if nums.count(0)==1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]=0
                else:
                    nums[i]=s
        else:
            for i in range(len(nums)):
                nums[i]=s//nums[i]
        return nums