class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return([-1,-1])
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        return([arr[0],arr[-1]])
