class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        a = []
        for i in range(len(arr)-1):
            a.append(abs(arr[i]-arr[i+1]))
        z = min(a)
        x = []
        for i in range(len(arr)-1):
            y = []
            if abs(arr[i]-arr[i+1])==z:
                y.append(arr[i])
                y.append(arr[i+1])
            if len(y)!=0:
                x.append(y)
        return x