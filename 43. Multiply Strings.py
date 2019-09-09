class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if int(num1) == 0 or int(num2) == 0:
            return str(0)

        num = []
        k = len(num1) - 1
        for i in num1:
            num.append(int(i)*pow(10, k))
            k -= 1

        res = 0
        for j in num:
            res += j * int(num2)

        return str(res)
