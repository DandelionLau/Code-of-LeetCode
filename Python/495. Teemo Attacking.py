"""
@FileName: 495. Teemo Attacking.py
@Description: Implement 495. Teemo Attacking
@Author: Ryuk
@CreateDate: 2021/06/20
@LastEditTime: 2021/06/20
@LastEditors: Please set LastEditors
@Version: v0.1
"""

from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0: return 0

        time = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration < timeSeries[i+1]:
                time += duration
            else:
                time += timeSeries[i+1] - timeSeries[i]

        return time + duration


def main():
    timeSeries = [1,2,3]
    duration = 2
    sol = Solution()
    result = sol.findPoisonedDuration(timeSeries, duration)
    print(result)



if __name__ == '__main__':
    main()
