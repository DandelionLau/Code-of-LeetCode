class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        tmp = nums[0:k]
        tmp.sort()

        for i in range(k, len(nums)):
            if nums[i] > tmp[0]:
                tmp.pop(0)
                tmp.append(nums[i])
                tmp.sort()

        return tmp[0]
