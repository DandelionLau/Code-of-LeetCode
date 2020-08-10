class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = 0
        if seats[0] == 0:
            left = -1
        else:
            left = 0

        for i in range(1, len(seats)):
            if seats[i] == 1:
                if left == -1:
                    distance = max(distance, i - left - 1)
                else:
                    distance = max(distance, (i - left) // 2)
                left = i
        if seats[-1] == 0:
            distance = max(distance, len(seats) - left - 1)

        return distance
