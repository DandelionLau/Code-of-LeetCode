class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0: break  # 1. because of j > i > k.
            if i > 0 and nums[i] == nums[i - 1]: continue  # 2. skip the same `nums[k]`.

            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                else:
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
        return res
