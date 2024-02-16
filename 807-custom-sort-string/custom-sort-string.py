class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = list(order)
        s = list(s)
        val = ''
        for j in order:
            for i in range(s.count(j)):
                val += j
                s.remove(j)
        return val + "".join(s)