class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        length = pow(2, n)
        if length == 1:
            return [0]


        res = [0] * length
        for i in range(1, length):
            res[i] = i ^ (i >> 1)

        return res
