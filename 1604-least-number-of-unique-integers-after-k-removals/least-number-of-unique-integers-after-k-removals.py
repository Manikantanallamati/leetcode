class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict = {}
        for i in range(len(arr)):
            if arr[i] not in dict:
                dict[arr[i]] = 1
            else:
                dict[arr[i]] += 1
        nums = sorted(dict.values())
        for count in range(len(nums)):
            if k>=nums[count]:
                k -= nums[count]
            else:
                return len(nums)-count
        return 0
        