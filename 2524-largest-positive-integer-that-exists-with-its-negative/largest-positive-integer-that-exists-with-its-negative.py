class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                if nums[i] == nums[j] - nums[j]*2:
                    arr.append(nums[j])
        return -1 if len(arr)==0 else max(arr)