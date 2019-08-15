class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return nums

        
        res = []
        for i in range(len(nums) - k + 1):
            tmp = nums[i:i+k]
            res.append(max(tmp))

        return res
