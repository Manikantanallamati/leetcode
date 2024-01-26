class Solution:
    def frequencySort(self, s: str) -> str:
        a = []
        b = []
        sets = list(set(s))
        ans = ''
        for i in sets:
            a.append(s.count(i))
            b.append(i)
        for i in range(len(a)):
            index = a.index(max(a))
            ans +=str(b[index])*(max(a))
            b.remove(b[index])
            a.remove(max(a))
        return ans