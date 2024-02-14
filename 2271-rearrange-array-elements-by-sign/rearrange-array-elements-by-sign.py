class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i]>=0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        nums.clear()
        for i in range(len(pos)):
            nums.append(pos[i])
            nums.append(neg[i])
        return nums 