class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = ''
        while columnNumber>26:
            if columnNumber%26==0:
                a+='Z'
                columnNumber-=1
            else:
                a+=chr((columnNumber%26)+64)
            columnNumber=columnNumber//26
        a+=chr((columnNumber)+64)
        return (a[::-1])
        # return ''