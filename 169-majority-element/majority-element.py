class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = list(set(nums))
        b = []
        c = []
        for i in range(len(a)):
            if nums.count(a[i])>(len(nums)//2):
                b.append(a[i])
                c.append(nums.count(a[i]))
        print(b)
        if len(b) == 0:
            return -1
        z = max(c)
        y = c.index(z)
        print(y)
        return b[y]