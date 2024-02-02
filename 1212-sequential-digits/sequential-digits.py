class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        a = []
        for i in range(len(digits)):
            for j in range(i+1,len(digits)+1):
                if int(digits[i:j])>=low and int(digits[i:j])<=high:
                    a.append(int(digits[i:j]))
        return sorted(a)

