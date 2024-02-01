class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        count = 0
        n = len(nums)
        if len(nums)<3:
            return []
        a = []
        for i in range(0,len(nums)-2,3):
                a.append(nums[i:i+3])
        for i in a:
            # if abs(nums[i+1]-nums[i])<=k and i == n-2:
            #     count+=1
            # elif i==n-2:
            #     return []
            # elif (nums[i+1]-nums[i])<=k and (nums[i+2]-nums[i])<=k:
            #     count+=1
            # else:
            #     return []
        # if count == len(nums)-1:
            if i[1]-i[0]<=k and i[2]-i[0]<=k:
                count+=1
        if count==len(a):
            return a
        else:
            return []