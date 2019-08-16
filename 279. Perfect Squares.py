class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        sq_nums = []
        for i in range(1, n):
            tmp = i ** 2
            if tmp > n:
                break
            else:
                sq_nums.append(i**2)

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            if i in sq_nums:
                dp[i] = 1
                continue
            else:
                tmp = []
                for j in range(len(sq_nums)):
                    if sq_nums[j] <= i:
                        tmp.append(dp[i - sq_nums[j]] + 1)
            dp[i] = min(tmp)
        return dp[n]
