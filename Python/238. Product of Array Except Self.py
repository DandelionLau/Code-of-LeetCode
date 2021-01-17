class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = []
        i = 0
        while i < n:
            if i == 0:
                left[i] = nums[i]
                right[n-i-1] = nums[n-i-1]
            else:
                left[i] = left[i-1] * nums[i]
                right[n-i-1] = right[n-i] * nums[n-i-1]
            i += 1

        for i in range(n):
            if i == 0:
                res.append(right[i+1])
            elif i == n - 1:
                res.append(left[i-1])
            else:
                res.append(left[i-1] * right[i+1])
        return res
