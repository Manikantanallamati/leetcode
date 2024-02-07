class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = num//3
        # print(a)
        if (3*a)==num:
            return [a-1,a,a+1]
        else:
            return []