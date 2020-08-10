class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 0:
            return
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])


        dp = [cost[0]]
        dp.append(cost[1])
        for i in range(2, n):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        return min(dp[-1], dp[-2])
