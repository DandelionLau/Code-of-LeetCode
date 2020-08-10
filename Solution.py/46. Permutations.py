# DFS

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        res = []
        for i in range(len(nums)):
            path = []
            self.dfs(nums, visited, path, res)
            visited[i] = 1

        return res

    def dfs(self, nums, visited, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if visited[i] == 0:
                path.append(nums[i])
                visited[i] = 1
                self.dfs(nums, visited, path, res)
                path.pop()
                visited[i] = 0
