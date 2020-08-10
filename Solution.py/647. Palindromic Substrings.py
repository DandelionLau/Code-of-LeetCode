class Solution(object):
    def countSubstrings(self, s):
        self.res = 0
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            self.spread(s, i, i)
            self.spread(s, i, i+1)

        return self.res


    def spread(self, nums, i, j):
        if 0 <= i and j < len(nums):
            if nums[i] == nums[j]:
                self.res += 1
                self.spread(nums, i - 1, j + 1)
