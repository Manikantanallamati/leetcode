class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = nums1+nums2
        count = 0
        for i in range(len(nums1)):
            if a[i]==0 :
                count+=1
        for i in range(len(nums2)):
            a.remove(0)
        nums1.clear()
        a = sorted(a)
        nums1+=a
        # nums1 = sorted(nums1)