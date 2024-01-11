class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a = []
        if k == 1:
            return max(nums)
        s = sum(nums[0:k])
        val = -99999999
        j=0
        for i in range(k,len(nums)):
            val=max(val,s/k)
            s-=nums[j]
            j+=1
            s+=nums[i]
        val=max(val,s/k)
        return val