class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = triangle[-1]
        i = n-2

        while i >=0:
            j = 0
            while j <= len(triangle[i])-1:
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
                j += 1
            i -= 1
        return dp[0]
