class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0:
            return []

        n = len(matrix[0])

        a = 0
        b = n
        c = m
        while len(res) < m * n:
            # 打印上边
            for j in range(a, b):
                res.append(matrix[a][j])
            if len(res) >= m * n:
                break

            # 打印右边
            for k in range(a+1, c):
                res.append(matrix[k][b-1])
            if len(res) >= m * n:
                break

            # 打印下边
            for t in range(b-2, a-1, -1):
                res.append(matrix[c-1][t])
            if len(res) >= m * n:
                break

            # 打印左边
            for s in range(c-2, a, -1):
                res.append(matrix[s][a])
            if len(res) >= m * n:
                break

            a += 1
            b -= 1
            c -= 1
        return res
