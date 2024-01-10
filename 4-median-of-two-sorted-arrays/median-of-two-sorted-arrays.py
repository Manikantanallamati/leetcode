class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(list(nums1)+(list(nums2)))
        if len(a)%2==0:
            z = len(a)//2
            b = (a[z-1]+a[z])/2
            return b
        else:
            c = len(a)//2
            d = a[c]
            return d