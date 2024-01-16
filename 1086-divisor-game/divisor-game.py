class Solution:
    def divisorGame(self, n: int) -> bool:
        if n==1:
            return False
        return (n-1)%2