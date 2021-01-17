class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        index = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
            else:
                nums[index] = nums[i]
                index += 1
                i = i + 1
        return index
            
