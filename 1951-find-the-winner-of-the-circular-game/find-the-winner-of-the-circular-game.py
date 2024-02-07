class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        values = [i for i in range(1,n+1)]
        i = k-1
        while len(values) != 1:

            # print(values)
            values.pop(i)
            i = (i+(k-1))%len(values)

        print(values)
        return values[0]