class Solution:
    def isValid(self, s: str) -> bool:
        
        if s == "":
            return True

        data = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}
        stack = []
        bracket = list(s)
        i = 0
        j = -1

        while i < len(bracket):
            if j == -1:
                stack.append(bracket[i])
                j = j + 1
            else:
                if data[stack[j]] + data[bracket[i]] == 0:
                        del stack[j]
                        j = j - 1
                else:
                        stack.append(bracket[i])
                        j = j + 1
            i = i + 1
        if len(stack) == 0:
            return True
        else:
            return False
