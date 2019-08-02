# dp

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return True

        dp = [False] * len(nums)
        if nums[0] > 0:
            dp[0] = True
            self.fillTrue(dp, 0+1, 0+nums[0]+1)
        else:
            return False
        
        end = 0+nums[0]
        for i in range(1, len(nums)):
            if i+nums[i] <= end:
                continue
            if nums[i] > 0 and dp[i]:
                self.fillTrue(dp, i+1, i+nums[i]+1)
        return dp[-1]


    def fillTrue(self, dp, start, end):
        for i in range(start, end):
            if i<len(dp) and dp[i] == True:
                continue
            if i < len(dp):
                dp[i] = True
            else:
                break
