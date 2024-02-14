class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        count = 0
        val = 0
        for i in range(len(word)-1):
            if val == 1:
                val = 0
                continue
            if abs(ord(word[i])-ord(word[i+1]))<2:
                count += 1
                print(word[i],word[i+1])
                val +=1
        return count