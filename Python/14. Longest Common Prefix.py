class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        for i in range(len(strs)-1):
            temp = ""
            for j in range(len(min(strs[i], strs[i+1]))):
                if strs[i][j] == strs[i+1][j]:
                    temp = temp + strs[i][j]
                else:
                    break
            if i == 0:
                prefix = temp
            elif len(temp)<len(prefix):
                prefix = temp
        return prefix
 
                
