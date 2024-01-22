class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for i in nums:
            if i in b:
                a.append(i)
                break
            else:
                b.append(i)
        c = list(set(nums))
        a.append((len(nums)*(len(nums)+1)//2-sum(c)))
        return a