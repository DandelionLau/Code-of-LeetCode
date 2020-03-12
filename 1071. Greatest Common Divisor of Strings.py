from typing import List

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        j = 0
        gcd = ""
        tmp = ""
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                tmp += str1[i]
                i += 1
                j += 1
                if len(gcd) < len(tmp) and (len(str2) % len(tmp) == 0 and len(str1) % len(tmp) == 0):
                    gcd = tmp
            else:
                return ""

        if i == len(str1):
            k = 0
            while j < len(str2):
                if k == len(tmp): k = 0
                if str2[j] != tmp[k]:
                    return ""
                j += 1
                k += 1

        if j == len(str2):
            k = 0
            while i < len(str1):
                if k == len(tmp): k = 0
                if str1[i] != tmp[k]:
                    return ""
                i += 1
                k += 1

        return gcd


def main():
    str1 = "ABABAB"
    str2 = "ABAB"
    sol = Solution()
    result = sol.gcdOfStrings(str1, str2)
    print(result)



if __name__ == '__main__':
    main()
