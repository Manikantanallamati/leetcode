class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # a = Counter(nums)
        # b = []
        # for i in nums:
        #     if a[i]==2:
        #         if i not in b:
        #             b.append(i)
        # return a,b
        s=set()
        l=[]
        for i in nums:
            if i in s:l.append(i)
            s.add(i)
        return l