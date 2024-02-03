class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = [1]*5
        for i in range(n-1):
            for j in range(5):
                a[j] = sum(a[j:])
        return sum(a)