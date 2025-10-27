class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        arr = []
        for i in range(len(bank)):
            count = bank[i].count('1')
            if count:
                arr.append(count)
        if len(arr) <= 1:
            return 0
        for i in range(len(arr)-1):
            ans += arr[i] * arr[i+1]
        return ans