class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r = len(word1) + 1
        c = len(word2) + 1
        dp = [([0] * (c)) for i in range(r)]

        for i in range(r):
            for j in range(c):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1) + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]
