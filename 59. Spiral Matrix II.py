class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [([0] * n) for _ in range(n)]
        visited = [([0] * n) for _ in range(n)]

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        k = 1
        while k <= n*n:
            res[r][c] = k
            k += 1
            visited[r][c] = 1
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and visited[cr][cc] == 0:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return res
