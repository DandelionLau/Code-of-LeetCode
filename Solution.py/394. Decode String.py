class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        char_stack = []
        res = ""
        t = ''
        for c in s:
            if c == '[':
                char_stack.append(c)
                num_stack.append(int(t))
                t = ''
            elif c == ']':
                tmp = ""
                while char_stack[-1] != '[':
                    tmp = char_stack.pop() + tmp
                char_stack.pop()            # pop '['
                k = num_stack.pop()
                tmp *= k
                char_stack.append(tmp)
            elif (c < 'a' or c > 'z') and (c < 'A' or c > 'Z'):               # number
                t = t + c
            elif 'a' <= c <= 'z' or 'A' <= c <= 'Z':               # char
                char_stack.append(c)

        res = ''.join(str(t) for t in char_stack)
        return res
