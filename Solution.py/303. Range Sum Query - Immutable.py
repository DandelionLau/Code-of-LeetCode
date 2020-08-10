class NumArray:
    def __init__(self, nums):
        if len(nums) == 0:
            return 
        self.nums = nums
        dp = [nums[0]]
        for i in range(1, len(nums)):
            temp = dp[i-1] + nums[i]
            dp.append(temp)
        self.dp = dp

    def sumRange(self, i: int, j: int):
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]
