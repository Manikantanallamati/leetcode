class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        a = []
        for i in range(2**len(nums)):
            b = []
            for j in range(len(nums)):
                if i & (1<<j):
                    b.append(nums[j])
            b.sort()
            if b not in a:
                a.append(b)
        return a