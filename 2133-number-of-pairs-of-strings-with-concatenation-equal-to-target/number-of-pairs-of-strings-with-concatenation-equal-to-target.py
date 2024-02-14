class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target and nums[j]+nums[i]==target:
                    count+= 2
                elif nums[i]+nums[j] == target:
                    count +=1
                elif nums[j]+nums[i] == target:
                    count +=1
                    # print(nums[i],nums[j],nums[i]+nums[j])
        return count 