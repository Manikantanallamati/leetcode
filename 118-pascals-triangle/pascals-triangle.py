def Recur(val,numRows,b):
    if val == numRows+1:
        return b
    array = [1]*val
    k = 0
    for i in range(len(array)-2):
        array[i+1] = b[val-2][k]+b[val-2][k+1]
        k+=1
    b.append(array)
    Recur(val+1,numRows,b)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return[[1]]
        elif numRows==2:
            return[[1],[1,1]]
        b = [[1],[1,1]]
        ans = Recur(3,numRows,b)
        return b
