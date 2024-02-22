class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        z = [0 for i in range(n+1)]
        y = [0 for i in range(n+1)]
        for a,b in trust:
            z[a] = 1
            y[b] += 1
        z[0]=1
        if z.count(0)>1 or z.count(0)<1:
            return -1
        for i in range(1,n+1):
            if z[i]==0:
                if y[i]>= n-1:
                   return i 
        return -1