def call(val,rowIndex,b):
    if val == rowIndex+2:
        return b
    array = [1]*val
    k = 0
    for i in range(len(array)-2):
        array[i+1]=b[val-1][k]+b[val-1][k+1]
        k+=1
    b.append(array)
    call(val+1,rowIndex,b)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        b = [[1],[1,1]]
        call(2,rowIndex,b)
        return b[-1]