class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a,b = 0,0
        b = []
        # sets = list(set(nums))
        for i in nums:
            if i in b:
                a=i
                break
            else:
                b.append(i)
        c = list(set(nums))
        b = ((len(nums)*(len(nums)+1)//2-sum(c)))
        return [a,b]