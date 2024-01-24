class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in arr:
            if arr.count(i)==1:
                k -=1
            if k ==0:
                return i
        else:
            return ''