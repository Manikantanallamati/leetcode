class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n == 3:
            if nums[0]+nums[1]>nums[2]:
                return sum(nums)
            else:
                return -1
        val = sum(nums[:n-1])
        for i in range(n-2,-1,-1):
            print(val,nums[i+1],nums)
            if val>nums[i+1]:
                return val+nums[i+1]
            else:
                val -= nums[i]
        return -1