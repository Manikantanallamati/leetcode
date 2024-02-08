class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0 
        n = len(prices)
        for i in range(1,n):
            cost = prices[i]-mini
            if profit<cost:
                profit = cost
            # profit = max(profit,cost)
            if mini>prices[i]:
                mini = prices[i]
            # mini = min(mini,prices[i])
        return profit