class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        diff = 2
        prev = 2
        count = 1
        temp = 2
        ans = 4
        for i in range(5,n+1):
            ans+=temp
            if count%3==0:
                prev = prev*3
                temp=prev
                count+=1
            else:
                temp = (prev*3)//2
                count +=1
        return ans
