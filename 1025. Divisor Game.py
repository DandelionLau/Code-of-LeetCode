class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [0] * (N+1)

        if N == 1:
            return False
        if N == 2:
            return True
        if N == 3:
            return False

        dp[1] = 1
        dp[2] = 1
        dp[3] = 0
        for i in range(4, N+1):
            index = self.getdivisors(i)
            if len(index) == 1:
                dp[i] = 1 - dp[i-1]     # if there is only one divisor, the result is contary to N-1
            else:
                # if there are more than one divisiors, if there is one false in the divisors, the result is true, else, false 
                dp[i] = 1 - min([dp[val] for val in index])

        if dp[-1] == 1:
            return True
        else:
            return False
        
    # get the divisior of N
    def getdivisors(self, N):
        divisors = []
        for i in range(1, N):
            if N % i == 0:
                divisors.append(N - i)
        return divisors
