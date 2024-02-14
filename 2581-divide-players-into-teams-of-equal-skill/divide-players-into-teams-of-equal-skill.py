class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        a = 0
        z = []
        for i in range(len(skill)//2):
            a += skill[i]*skill[-i-1]
            z.append(skill[i]+skill[-i-1])
        if 1 == len(set(z)):
            return a
        else:
            return -1