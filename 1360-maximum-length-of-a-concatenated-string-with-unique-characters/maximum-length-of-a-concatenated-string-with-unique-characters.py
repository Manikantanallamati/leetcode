class Solution:
    def maxLength(self, arr: List[str]) -> int:
        a = 2**len(arr)
        s = 0
        for i in range(a-1,0,-1):
            d = ''
            for j in range(len(arr)):
                if i & 1<<j:
                    d+=arr[j]
            if len(d) == len(list(set(d))):
                s = max(s,len(d))
        return s
