class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            len1, l1, r1 = self.centerSpread(s, i, i)
            len2, l2, r2 = self.centerSpread(s, i, i+1)
            if len1 > len2:
                tmp = s[l1:r1+1]
            else:
                tmp = s[l2:r2+1]

            if len(tmp) > len(res):
                res = tmp

        return res


    def centerSpread(self, s, i, j):
        res = 0
        if i >= 0 and j < len(s) and s[i] != s[j]:

            return res, i, j
        else:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res, i+1, j-1
