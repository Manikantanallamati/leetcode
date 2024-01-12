class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = [0]*len(s)
        for i in range(len(s)):
            # a.insert(indices[i],s[i])
            a[indices[i]] = s[i]
        a = "".join(a)
        return a