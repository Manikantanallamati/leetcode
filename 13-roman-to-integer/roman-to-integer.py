class Solution:
    def romanToInt(self, s: str) -> int:
        SymList ={
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'LC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000}
        count = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for Sym in s:
            count+=SymList[Sym]
        return count
