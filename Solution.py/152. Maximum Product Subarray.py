class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return

        max_dp = [0] * (len(nums) + 1)
        min_dp = [0] * (len(nums) + 1)
        max_dp[0] = 1
        min_dp[0] = 1

        for i in range(1, len(nums) + 1):
            max_dp[i] = max(max_dp[i-1]*nums[i-1], min_dp[i-1]*nums[i-1], nums[i-1])
            min_dp[i] = min(max_dp[i-1]*nums[i-1], min_dp[i-1]*nums[i-1], nums[i-1])
        return max(max_dp[1:])
