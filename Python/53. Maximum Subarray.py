class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            if i == 0:
                dp.append(nums[i])
            else:
                dp.append(max(dp[i-1] + nums[i], nums[i]))
        return max(dp)
