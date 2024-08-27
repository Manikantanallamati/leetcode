class Solution:
    def findComplement(self, num: int) -> int:
        num = str(bin(num))[2:]
        ind = 0
        val = 0
        for i in range(len(num)-1,-1,-1):
            if num[i] == "0":
                # print(num[i])
                val += 2**ind
            ind += 1
        return val