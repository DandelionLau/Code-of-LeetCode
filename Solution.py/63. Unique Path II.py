class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [([0] * (n+1)) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                # print(i,j)
                if i == 1 and j == 1:
                    dp[i][j] = 1 - obstacleGrid[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j] * (1 - obstacleGrid[i-2][j-1]) + dp[i][j-1] * (1 - obstacleGrid[i-1][j-2])
        return dp[m][n]
