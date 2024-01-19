class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a = []
        for i in mat:
            a.append(i.count(1))
        c = []
        print(a)
        for j in range(k):
            c.append(a.index(min(a)))
            a.insert(a.index(min(a)),10000000000)
            a.pop(a.index(min(a)))
        print (a)
        return c
        
        # return a[0:k]