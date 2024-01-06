class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        b = []
        for i in range(2**len(nums)):
            a = []
            for j in range(len(nums)):
                if i & (1<<j):
                    a.append(nums[j])
            b.append(a)
        return b