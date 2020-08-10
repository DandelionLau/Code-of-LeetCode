class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True


        count = 0
        tmp = n
        while True:
            tmp = self.getNumber(tmp)
            if tmp == 1:
                return True
            count += 1
            if count > 500:
                return False

    def getNumber(self, n):
        res = 0
        k = 1
        while n >= 1:
            tmp = n % pow(10, k)
            n = n // pow(10, k)
            res += tmp * tmp
        return res
