class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m = max(arr) + k
        x = [i for i in range(1,m+1)]
        l = []
        for i in x:
            if i not in arr:
                l.append(i)
        return l[k-1]