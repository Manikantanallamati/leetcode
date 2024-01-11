class Solution:
    def trimMean(self, arr: List[int]) -> float:
        k = len(arr)//20
        return sum(sorted(arr)[k:-k]) /(18*k)