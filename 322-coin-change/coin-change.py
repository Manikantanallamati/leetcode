class Solution:
    def moon(self,l,i,t,d):
        m=10000000
        r=(i,t)
        if r in d:
            return d[r]
        if t==0:
            return 0
        if i==len(l):
            if t==0:
                return 0
            return 10000000
        if l[i]<=t:
            m=min(m,(self.moon(l,i,t-l[i],d))+1)
        m=min(m,self.moon(l,i+1,t,d))
        d[r]=m
        return m

    def coinChange(self, coins: List[int], amount: int) -> int:
        d={}
        a= self.moon(coins,0,amount,d)
        return -1 if a==10000000 else a