class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        if m == 0:
            self.dp = None
            return
        n = len(matrix[0])
        dp = []

        for i in range(m):
            row_dp = [matrix[i][0]]
            for j in range(1, n):
                row_dp.append(row_dp[j-1] + matrix[i][j])
            dp.append(row_dp)
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        i = row1
        while i <= row2:
            if col1 != 0:
                result += self.dp[i][col2] - self.dp[i][col1-1]
            else:
                result += self.dp[i][col2]
            i += 1
        return result
