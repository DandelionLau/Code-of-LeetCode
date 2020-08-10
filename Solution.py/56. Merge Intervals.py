# radix sort

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return [] if len(intervals) == 0 else intervals

        nums = sorted(intervals, key=lambda x: x[0])
        nums = sorted(nums, key=lambda x: x[1])

        res = []
        i = len(nums) - 2
        last = nums[-1]
        while True:
            if i == -1:
                if last[0] > nums[0][1]:
                    res.append(last)
                else:
                    res.append([min(last[0], nums[0][0]), max(last[1], nums[0][1])])
                break
            elif last[0] > nums[i][1]:
                res.append(last)
                last = nums[i]
            else:
                last = [min(last[0], nums[i][0]), max(last[1], nums[i][1])]
            i -= 1
        return res
