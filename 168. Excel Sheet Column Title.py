class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        if n <= 26:
            res = chr(n + 64)
        else:
            while n > 26:
                a = n % 26
                if a == 0:
                    res = 'Z' + res
                    n = n // 26 - 1
                else:
                    res = chr(a + 64) + res
                    n = n // 26
            res = chr(n + 64) + res
        return res
