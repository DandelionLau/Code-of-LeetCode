from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        total = [0] * len(A)
        acc = 0
        for i in range(len(A)):
            acc += A[i]
            total[i] = acc

        first = acc // 3
        second = 2 * acc // 3

        for i in range(len(total) - 1):
            if total[i] == first:
                for j in range(i+1, len(total) - 1):
                    if total[j] == second:
                        return True
        return False


def main():
    data = [
        [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], # true
        [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], # false
        [3, 3, 6, 5, -2, 2, 5, 1, -9, 4],    # true
        [6, 1, 1, 13, -1, 0, -10, 20],       # false
        [29, 31, 27, -10, -67, 22, 15, -1, -16, -29, 59, -18, 48], #true
        [14, 6, -10, 2, 18, -7, -4, 11], #false
        [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], #true
        [1, -1, 1, -1] #false
    ]
    sol = Solution()
    for nums in data:
        result = sol.canThreePartsEqualSum(nums)
        print(result)



if __name__ == '__main__':
    main()
