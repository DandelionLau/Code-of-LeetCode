# dfs
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        visited = [0] * len(nums)
        for i in range(len(nums)):
            if visited[i] == 0:
                path = [nums[i]]
                res.append(path)
                visited[i] = 1
                self.dfs(nums, visited[:], path, res)


        return res

    def dfs(self, nums, visited, tmp, res):
        if 0 not in visited:
            return
        for i in range(len(nums)):
            if visited[i] == 0:
                tmp.append(nums[i])
                res.append(tmp[:])
                visited[i] = 1
                self.dfs(nums, visited[:], tmp, res)
                tmp.pop()
