class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        i = 0
        for freq in c.values():
            if freq == 1:
                return -1
            i += ceil(freq / 3)
        return i