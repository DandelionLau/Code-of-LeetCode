from typing import List

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # for i in range(m, m+n):
        #     A[i] = B[i-m]
        # A.sort()

        # copy first elements to the end of A
        for i in range(1, m + 1):
            A[-i] = A[m - i]

        i = len(A) - m
        j = 0
        k = 0
        while i < len(A) and j < n:
            if A[i] < B[j]:
                A[k] = A[i]
                i += 1
            else:
                A[k] = B[j]
                j += 1
            k += 1

        # copy B's tail to A
        if i == len(A):
            while j < n:
                A[k] = B[j]
                j += 1
                k += 1



def main():
    A = [1, 2, 7, 0, 0, 0]
    m = 3
    B = [1, 5, 6]
    n = 3
    sol = Solution()
    sol.merge(A, m, B, n)
    print(A)



if __name__ == '__main__':
    main()
