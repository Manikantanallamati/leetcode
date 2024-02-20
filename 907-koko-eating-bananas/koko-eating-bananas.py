def Fun(piles,val,h):
    a = 0
    for i in range(len(piles)):
        if a >h:
            return False
        a+=(piles[i]//val)
        if(piles[i]%val !=0):a+=1
    return a<=h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # maxi = max(piles)
        low = 1
        high = max(piles)
        res=high
        while low<=high:
            mid = (low+high)//2
            if Fun(piles,mid,h):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res