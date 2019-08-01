class Solution:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        buy = prices[0]
        dp = [0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            dp.append(max(dp[i-1], prices[i] - buy))

        return max(dp)
