class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = list(set(arr))
        a = []
        for i in s:
            a.append(arr.count(i))
        b = list(set(a))
        if len(a) == len(b):
            return True
        else:
            return False