class Solution:

    def maximumJumps(self, nums: List[int], target: int) -> int:

        n = len(nums)

        dp = [-1] * n

        def dfs(i):

            if i == n - 1:
                return 0

            if dp[i] != -1:
                return dp[i]

            max_jumps = -10**9

            for j in range(i + 1, n):

                if -target <= nums[j] - nums[i] <= target:

                    max_jumps = max(
                        max_jumps,
                        1 + dfs(j)
                    )

            dp[i] = max_jumps
            return dp[i]

        jumps = dfs(0)

        return -1 if jumps < 0 else jumps
