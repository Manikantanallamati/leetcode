class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        val = -1
        for i in range(k):
            if happiness[val]>0:
                ans += happiness[val]
            if len(happiness)!=abs(val):
                happiness[val-1]=happiness[val-1]+val
            val -= 1
        return ans