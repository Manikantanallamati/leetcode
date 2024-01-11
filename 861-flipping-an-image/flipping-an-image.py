class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        z = []
        for i in image:
            a = []
            s = i[::-1]
            for j in s:
                if j == 0:
                    a.append(1)
                else:
                    a.append(0)
            z.append(a)
            print(a)
        return z