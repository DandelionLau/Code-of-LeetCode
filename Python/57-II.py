from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        acc = {0:0}
        res = []
        sum = 0
        for i in range(1, target//2 + 2):
            sum += i
            acc[sum] = i

        for num in acc.keys():
            if target + num in acc and acc[num] != acc[target + num]:
                res.append([x for x in range(acc[num] + 1, acc[target + num] + 1)])

        return res


def main():
    target = 15
    sol = Solution()
    result = sol.findContinuousSequence(target)
    print(result)



if __name__ == '__main__':
    main()
