### Python

```python
import math

class Solution:
    kMod = 1_000_000_007
    kMaxNum = 200
    
    # Precompute GCDs to avoid recalculation in DP loop.
    kGcdTable = [[0] * (kMaxNum + 1) for _ in range(kMaxNum + 1)]
    for j1 in range(kMaxNum + 1):
        for j2 in range(kMaxNum + 1):
            if j1 == 0:
                kGcdTable[j1][j2] = j2
            elif j2 == 0:
                kGcdTable[j1][j2] = j1
            else:
                kGcdTable[j1][j2] = math.gcd(j1, j2)

    # Modulo addition helper.
    def addMod(self, lhs: int, rhs: int) -> int:
        lhs += rhs
        return lhs - self.kMod if lhs >= self.kMod else lhs

    def subsequencePairCount(self, nums: List[int]) -> int:
        maxVal = max(nums)
        stride = maxVal + 1
        # Flattened 2D state size.
        totStates = stride * stride

        dp = [0] * totStates
        nextDp = [0] * totStates

        # Base case: both subsequences are empty (gcd 0).
        dp[0] = 1

        for num in nums:
            # Carry over states where num is skipped.
            nextDp[:] = dp

            for idx, cnt in enumerate(dp):
                if cnt == 0:
                    continue

                gcd1 = idx // stride
                gcd2 = idx % stride

                # Transition 1: append to first subsequence.
                nextGcd1 = self.kGcdTable[gcd1][num]
                idx1 = nextGcd1 * stride + gcd2
                nextDp[idx1] = self.addMod(nextDp[idx1], cnt)

                # Transition 2: append to second subsequence.
                nextGcd2 = self.kGcdTable[gcd2][num]
                idx2 = gcd1 * stride + nextGcd2
                nextDp[idx2] = self.addMod(nextDp[idx2], cnt)

            dp = nextDp.copy()

        result = 0
        # Sum states where both have the same non-zero GCD.
        for gcd_ in range(1, stride):
            result = self.addMod(result, dp[gcd_ * stride + gcd_])

        return result
