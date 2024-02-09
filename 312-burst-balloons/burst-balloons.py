from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        def max_coins(start, end):
            if start >= end - 1:
                return 0
            if dp[start][end] > 0:
                return dp[start][end]
            max_val = 0
            for i in range(start + 1, end):
                coins = nums[start] * nums[i] * nums[end]
                coins += max_coins(start, i) + max_coins(i, end)
                max_val = max(max_val, coins)
            dp[start][end] = max_val
            return max_val
        return max_coins(0, n - 1)
