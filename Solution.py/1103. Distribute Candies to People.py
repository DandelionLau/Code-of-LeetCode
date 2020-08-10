from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        round = 0
        while candies > 0:
            for i in range(len(res)):
                cur_distribute = round * num_people + i + 1
                if cur_distribute < candies:
                    res[i] += cur_distribute
                    candies -= cur_distribute
                else:
                    res[i] += candies
                    return res
            round += 1
        return res


def main():
    candies = 5
    num_people = 1
    sol = Solution()
    result = sol.distributeCandies(candies, num_people)
    print(result)



if __name__ == '__main__':
    main()
