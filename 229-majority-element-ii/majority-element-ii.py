class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = list(set(nums))
        b = []
        for i in range(len(a)):
            if len(nums)//3 < (nums.count(a[i])):
                b.append(a[i])
        return b