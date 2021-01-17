class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        x = bin(n)[2:]
        for c in x:
            if c == '1':
                count += 1
        return count
        
