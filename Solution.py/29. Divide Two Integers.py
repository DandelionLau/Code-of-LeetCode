class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
            flag = True
        else:
            flag = False

        result, remainder = self.predivide(dividend, divisor)
        while remainder >= abs(divisor):
            post_result, remainder = self.predivide(remainder, divisor)
            result = result + post_result
        return self.stackoveflow(flag, result)

    def predivide(self, dividend, divisor):
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        i = 0
        factor = 0
        while dividend >= divisor and dividend - factor >= 0:
            factor += divisor
            i += 1
            dividend -= factor
            count += i
        if dividend < 0:
            count -= 1
        return count, dividend

    def stackoveflow(self, flag, result):
        int_max = 2147483647
        int_min = -2147483648
        if flag:    # positive result
            return min(int_max, result)
        else:      # negative result
            return max(int_min, -result)
