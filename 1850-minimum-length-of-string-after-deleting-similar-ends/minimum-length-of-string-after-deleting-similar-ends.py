class Solution:
    def minimumLength(self, s: str) -> int:
        i , j = 0 , len(s)-1
        while i < j :
            ch = s[i]
            # if i == j:
            #     break
            if s[i] != s[j]:
                break 
            while i <= j and s[i]==ch:
                i += 1
            while i <= j and s[j] == ch:
                j -= 1
        return (j-i+1)