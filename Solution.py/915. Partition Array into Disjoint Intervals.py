class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        max_list = [float("-inf")] * len(A)
        max_list[0] = A[0]
        for i in range(1, len(A)):
            max_list[i] = max(max_list[i-1], A[i])

        min_list = [float("inf")] * len(A)
        min_list[-1] = A[len(A)-1]
        for i in range(len(A)-2, -1, -1):
            min_list[i] = min(min_list[i+1], A[i])

        for i in range(len(A)-1):
            if max_list[i] <= min_list[i+1]:
                return i + 1
        return 0
