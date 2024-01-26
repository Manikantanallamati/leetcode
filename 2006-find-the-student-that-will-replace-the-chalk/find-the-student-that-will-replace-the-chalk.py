class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k%sum(chalk)==0:
            return 0
        else:
            a = k%sum(chalk)
            for i in range(len(chalk)):
                if chalk[i]-a<=0:
                    a -= chalk[i]
                else:
                    return i