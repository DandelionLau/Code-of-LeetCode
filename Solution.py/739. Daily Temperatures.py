class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0] * len(T)
        stack = [0]
        for i in range(1, len(T)):
            while len(stack) > 0 and T[i] > T[stack[-1]]:
                tmp = stack.pop()
                res[tmp] = i - tmp
            stack.append(i)

        return res
