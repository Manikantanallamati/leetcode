class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            z = 0
            for j in range(len(mat[i])):
                if i == j :
                    count +=mat[i][j]
                elif i == len(mat)-j-1:
                    count+=mat[i][j]
        return count