class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        a = []
        count = 1
        for i in range(len(prices)-1):
            if prices[i]-1==prices[i+1]:
                count+=1
            else:
                count = 1
            a.append(count)
        return sum(a)+1