class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        count = 0
        a = []
        for i in range(1,len(nums)):
            if nums[i-1] == (nums[i]-1):
                count +=1
            else:
                count = 0
            a.append(count)
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]+1
        return max(a)+1