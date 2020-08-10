class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        d = len(s) - 1
        for c in s:
            res += (ord(c) - ord('A') + 1) * pow(26, d)
            d -= 1
        return res
