from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:           # if amount is 0, return 0
            return 0
        if amount < min(coins):
            return -1

        dp = [float("inf")] * (amount + 1)

        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            else:
                tmp = float("inf")
                for j in coins:
                    if i - j > 0:
                        if dp[i - j] != float("inf"):       # can change
                            tmp = min(tmp, dp[i-j] + 1)
            dp[i] = tmp

        if dp[-1] == float("inf"):
            return -1
        return dp[-1]


def main():
    coins = [1]
    amount = 1
    sol = Solution()
    result = sol.coinChange(coins, amount)
    print(result)



if __name__ == '__main__':
    main()
