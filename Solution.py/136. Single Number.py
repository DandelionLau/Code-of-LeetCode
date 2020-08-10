class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 1
        res = nums[0]
        while i < len(nums):
            res = res ^ nums[i]
            i += 1
        return res
