class Solution:
    def nextGreatestLetter(self, let: List[str], tar: str) -> str:
        li = []
        for i in range(len(let)):
            if ord(let[i]) > ord(tar):
                return let[i]
        return let[0]
        