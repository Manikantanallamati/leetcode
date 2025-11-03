class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        arr = [neededTime[0]]
        ans = 0
        for i in range(1,len(colors)):
            if colors[i-1] == colors[i]:
                arr.append(neededTime[i])
            elif colors[i-1] != colors[i]:
                if len(arr) != 1:
                    ans += (sum(arr) - max(arr))
                    arr.clear()
                    arr.append(neededTime[i])
                else:
                    arr.clear()
                    arr.append(neededTime[i])
        if len(arr) != 1:
            ans += (sum(arr) - max(arr))
        return ans