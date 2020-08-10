class Solution:
    def removeElement(self, nums, val: int) -> int:
        count = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[j] == val:
                while j > 0 and nums[j] == val:
                    j -= 1
                    count += 1
            if nums[i] == val:
                count += 1
                nums[i] = nums[j]
                nums[j] = val
                j -= 1
            else:
                i += 1
        return len(nums) - count
