class Solution:
    def searchRange(self, nums, target: int):
        left_idx = self.searchBounder(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.searchBounder(nums, target, False) - 1]


    def searchBounder(self, nums, target, flag):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target or nums[mid] == target and flag:
                right = mid
            else:
                left = mid+1

        return left
