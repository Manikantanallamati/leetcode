class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        k=[]
        d={}
        for i in matches:
            if i[1] in d:
                d[i[1]]+=1
            else:
                d[i[1]]=0
            k.append(i[0])
            k.append(i[1])
        k=sorted(list(set(k)))
        p,g=[],[]
        s=[]
        for i in k:
            try:
                if(d[i]==0):
                    p.append(i)
            except:
                g.append(i)
        s.append(g)
        s.append(p)
        return s