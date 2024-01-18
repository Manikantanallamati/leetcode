class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if list(set(nums))==nums and valueDiff==0:
            return False
        bucket = {}
        width = valueDiff+1
        for i,n in enumerate(nums):
            bucket_i=n//width
            if bucket_i in bucket: return True
            elif bucket_i+1 in bucket and abs(n-bucket[bucket_i+1])<width:return True
            elif bucket_i-1 in bucket and abs(n-bucket[bucket_i-1])<width:return True
            bucket[bucket_i]=n
            if i>=indexDiff:del bucket[nums[i-indexDiff]//width]
        return False
        