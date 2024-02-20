class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s = sorted(nums)
        # for i in range(len(s)):
        #     if i not in s:
        #         return i
        #         break
        # return max(s)+1
        return (len(nums)*(len(nums)+1)//2) -sum(nums)