class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                for j in range(n):
                    if matrix[i][j] == target:
                        return True
        return False
