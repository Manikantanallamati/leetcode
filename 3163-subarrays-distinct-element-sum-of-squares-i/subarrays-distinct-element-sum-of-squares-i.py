class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum = 0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                arr = len(set(nums[i:j+1]))
                sum += arr*arr
        return sum