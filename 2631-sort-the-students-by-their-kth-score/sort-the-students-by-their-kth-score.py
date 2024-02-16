class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        maxi = []
        z = []
        for i in score:
            maxi.append(i[k])
        # print(maxi)
        for i in range(len(maxi)): 
            ind = maxi.index(max(maxi))
            z.append(score[ind])
            maxi[ind] = 0
        # print(z)
        return z