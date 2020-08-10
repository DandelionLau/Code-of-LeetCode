# first mirror, then exchange numbers according to diagonal line y = x

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)-1
        c = len(matrix[0])-1
        # mirror
        for i in range(r+1):
            for j in range((c+1)//2):
                matrix[i][j], matrix[i][c-j] = matrix[i][c-j], matrix[i][j]

        # exchange according diagonal line
        for i in range(r):
            for j in range(c+1):
                if i + j != c:
                    matrix[i][j], matrix[r-j][c-i] = matrix[r-j][c-i], matrix[i][j]
                else:
                    break
