class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = []
        for i in grid:
            for j in i:
                a.append(j)
        a.sort()
        b = list(set(a))
        b.append(0)
        print(a)
        c = []
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                c.append(a[i])
        for i in range(1,len(b)+1):
            if i != b[i-1]:
                c.append(i)
                break
        return c