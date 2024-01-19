class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        b = []
        for i in nums:
            if a[i]==2:
                if i not in b:
                    b.append(i)
        return b