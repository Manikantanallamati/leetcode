class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        count = 0
        start = 0
        tokens.sort()
        end = len(tokens)-1
        if len(tokens) == 0:
            return 0
        while start<end:
            print(start,end,power,count)
            # if count<0:
                # count += 1
                # break
            if tokens[start]<power and count>=0:
                power -= tokens[start]
                count+=1
                start += 1
            elif count>=1:
                power += tokens[end]
                count -= 1
                end -= 1
            else:
                break
        if tokens[start]<=power:
            count+=1
        return count