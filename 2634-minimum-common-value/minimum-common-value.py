class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums = set(nums2)
        for i in nums1:
            if i in nums:
                return i
        return -1