class Solution:
    def maxSumDivThree(self, nums):
        n = len(nums)
        dp = [[None] * 3 for _ in range(n)]

        from functools import lru_cache

        @lru_cache(None)
        def solve(i, rem):
            if i == n:
                return 0 if rem == 0 else -10**15

            notTake = solve(i + 1, rem)
            newRem = (rem + nums[i]) % 3
            take = nums[i] + solve(i + 1, newRem)

            return max(take, notTake)

        return solve(0, 0)
