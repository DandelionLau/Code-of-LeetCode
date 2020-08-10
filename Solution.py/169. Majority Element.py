class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        
        data = {}
        res = []
        n = len(nums)
        for i in nums:
            data[i] = data.get(i, 0) + 1
            if data[i] > n//2:
                return i

        
