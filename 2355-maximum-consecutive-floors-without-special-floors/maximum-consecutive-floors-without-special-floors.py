class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = sorted(special)
        a = special[0]-bottom
        b = top-special[-1]
        c = []
        for i in range(len(special)-1):
            c.append(special[i+1]-special[i])
        if len(c)>0:
            d = max(c)-1
            return max(a,b,d)
        else:
            return max(a,b)