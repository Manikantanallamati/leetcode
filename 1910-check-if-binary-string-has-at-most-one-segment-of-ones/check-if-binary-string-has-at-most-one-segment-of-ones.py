class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '1' not in s[s.index('0'):] if '0' in s else True