class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1,num+1):
            i = str(i)
            val = 0
            for j in i:
                val += int(j)
            if val%2==0:
                count +=1
        return count