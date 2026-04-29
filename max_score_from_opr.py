class Solution:
    def maximumScore(self, grid):
        n = len(grid[0])
        if n == 1:
            return 0

        # dp[i][currH][prevH]
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]

        prevMax = [[0] * (n + 1) for _ in range(n + 1)]
        prevSuffixMax = [[0] * (n + 1) for _ in range(n + 1)]

        # Column prefix sums
        colSum = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(1, n + 1):
                colSum[c][r] = colSum[c][r - 1] + grid[r - 1][c]

        for i in range(1, n):
            for currH in range(n + 1):
                for prevH in range(n + 1):

                    if currH <= prevH:
                        extraScore = colSum[i][prevH] - colSum[i][currH]
                        dp[i][currH][prevH] = max(
                            dp[i][currH][prevH],
                            prevSuffixMax[prevH][0] + extraScore
                        )
                    else:
                        extraScore = colSum[i - 1][currH] - colSum[i - 1][prevH]
                        dp[i][currH][prevH] = max(
                            dp[i][currH][prevH],
                            prevSuffixMax[prevH][currH],
                            prevMax[prevH][currH] + extraScore
                        )

            # Update prevMax and prevSuffixMax
            for currH in range(n + 1):
                prevMax[currH][0] = dp[i][currH][0]

                for prevH in range(1, n + 1):
                    if prevH > currH:
                        penalty = colSum[i][prevH] - colSum[i][currH]
                    else:
                        penalty = 0

                    prevMax[currH][prevH] = max(
                        prevMax[currH][prevH - 1],
                        dp[i][currH][prevH] - penalty
                    )

                prevSuffixMax[currH][n] = dp[i][currH][n]

                for prevH in range(n - 1, -1, -1):
                    prevSuffixMax[currH][prevH] = max(
                        prevSuffixMax[currH][prevH + 1],
                        dp[i][currH][prevH]
                    )

        ans = 0
        for k in range(n + 1):
            ans = max(ans, dp[n - 1][n][k], dp[n - 1][0][k])

        return ans
