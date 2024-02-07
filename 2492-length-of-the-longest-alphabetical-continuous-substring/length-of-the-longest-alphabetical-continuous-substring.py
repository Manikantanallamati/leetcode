class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        li = []
        count = 1
        for i in range(len(s)-1):
            a = ord(s[i])
            if a+1 == ord(s[i+1]):
                count +=1
            else:
                count = 1
            li.append(count)
        if len(s)==1:
            return 1
        print(li)
        return max(li)