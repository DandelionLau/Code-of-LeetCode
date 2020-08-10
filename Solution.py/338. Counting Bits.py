class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, num+1):
            res.append(self.getOne(i))
        
        return res


    def getOne(self, n):
        x = bin(n)[2:]
        count = 0
        for c in x:
            if c == '1':
                count += 1
        return count

