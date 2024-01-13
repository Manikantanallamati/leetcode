class Solution:
    def minSteps(self, s: str, t: str) -> int:
        m = []
        count = 0
        for i in s:
            if i not in m:
                if s.count(i)>t.count(i):
                    count+=abs(t.count(i)-s.count(i))
                m.append(i)
        return count