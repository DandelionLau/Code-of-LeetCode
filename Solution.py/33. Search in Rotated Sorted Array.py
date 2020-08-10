class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target: return 0
            else: return -1
        index = self.find_index(nums, 0, len(nums) - 1)
        if index == 0:
            return self.binart_search(nums, 0, len(nums)-1, target)
        if target >= nums[0]:
            return self.binart_search(nums, 0, index, target)
        else:
            return self.binart_search(nums, index, len(nums)-1, target)



    def binart_search(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

    def find_index(self, nums, low, high):
        if nums[low] < nums[high]:
            return 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid+1]:
                return mid + 1
            else:
                if nums[mid] < nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
