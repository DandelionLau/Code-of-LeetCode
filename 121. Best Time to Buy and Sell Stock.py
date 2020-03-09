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

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy = int(10e9)
#         res = 0
#         for i in range(len(prices)):
#             buy = min(buy, prices[i])
#             res = max(res, prices[i] - buy)
#         return res
