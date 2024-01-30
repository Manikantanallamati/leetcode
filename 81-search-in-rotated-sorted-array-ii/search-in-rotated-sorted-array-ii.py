class Solution:
    def search(self, nums: List[int], t: int) -> bool:
        nums.sort()
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l+h)//2
            if nums[m] == t:
                return True
            elif nums[m] < t:
                l = m + 1
            else:
                h = m - 1
        return False