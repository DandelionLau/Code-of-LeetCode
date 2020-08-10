from typing import List
import copy
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        fresh = 0
        last_rot = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    last_rot += 1

        while fresh != 0:
            minute += 1
            grid, fresh, cur_rot = self.Rotting(grid, fresh, last_rot)
            if last_rot == cur_rot:
                minute -= 1
                break
        if fresh == 0:
            return minute
        else:
            return -1

    def Rotting(self, grid, fresh, rot):
        matrix = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    if 0 <= i+1 < len(grid) and matrix[i+1][j] == 1:
                        matrix[i+1][j] = 2
                        rot += 1
                        fresh -= 1
                    if 0 <= i-1 < len(grid) and matrix[i-1][j] == 1:
                        matrix[i-1][j] = 2
                        rot += 1
                        fresh -= 1
                    if 0 <= j+1 < len(grid[0]) and matrix[i][j+1] == 1:
                        matrix[i][j+1] = 2
                        rot += 1
                        fresh -= 1
                    if 0 <= j-1 < len(grid[0]) and matrix[i][j-1] == 1:
                        matrix[i][j-1] = 2
                        rot += 1
                        fresh -= 1
        return matrix, fresh, rot




def main():
    grid = [[0, 1, 2]]
    sol = Solution()
    result = sol.orangesRotting(grid)
    print(result)



if __name__ == '__main__':
    main()
