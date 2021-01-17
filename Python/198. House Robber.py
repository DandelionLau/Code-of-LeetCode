class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp = [nums[0], max(nums[0], nums[1])]
            for i in range(2, len(nums)):
                dp.append(max(dp[i-1], dp[i-2] + nums[i]))
        return max(dp)
