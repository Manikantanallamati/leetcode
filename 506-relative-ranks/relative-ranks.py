class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = [0]*len(score)
        for i in range(1,len(a)+1):
            val = max(score)
            index = score.index(val)
            if i ==1:
                a[index]="Gold Medal"
            elif i==2:
                a[index]="Silver Medal"
            elif i ==3:
                a[index]="Bronze Medal"
            else:
                a[index] = str(i)
            score.remove(val)
            score.insert(index,-1)
        return a