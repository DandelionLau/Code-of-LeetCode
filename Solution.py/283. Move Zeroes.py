class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                start = max(flag, i+1)
                for j in range(start, len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        flag = j
                        break
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[count] == 0:
                    nums[count] = nums[i]
                    nums[i] = 0
                count += 1
        return nums
'''
