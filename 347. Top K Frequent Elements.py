class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data = {}
        for i in range(len(nums)):
            data[nums[i]] = data.get(nums[i], 0) + 1

        order = sorted(data.items(), key=lambda x:x[1], reverse=True)
        res = []
        for j in range(k):
            res.append(order[j][0])

        return res
