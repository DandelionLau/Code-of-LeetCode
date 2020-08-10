class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        while i < (len(haystack) - len(needle)) + 1:
            if haystack[i] == needle[0]:
                # continue matching
                j = 0
                start = i
                while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == len(needle):  # match successfully
                    return start
                else:
                    i = start + 1
            else:
                i += 1
        return -1
