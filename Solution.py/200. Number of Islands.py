class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [([0] * n) for _ in range(m)]

        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    k += 1
                    self.dfs(grid, visited, i, j)
        return k

    def dfs(self, grid, visited, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == '1' and visited[i][j] == 0:
                visited[i][j] = 1
                self.dfs(grid, visited, i - 1, j)
                self.dfs(grid, visited, i + 1, j)
                self.dfs(grid, visited, i, j - 1)
                self.dfs(grid, visited, i, j + 1)
