"""
@FileName: 69. Sqrt(x).py
@Description: Implement 69. Sqrt(x)
@Author: Ryuk
@CreateDate: 2021/06/27
@LastEditTime: 2021/06/27
@LastEditors: Please set LastEditors
@Version: v0.1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        for i in range(x//2+1):
            if i*i<=x<(i+1)*(i+1):
                return i


if __name__ == "__main__":
    x = 8
    solution = Solution()
    result = solution.mySqrt(x)
    print(result)