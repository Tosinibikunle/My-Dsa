class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                bit = (x + 1) & -(x + 1)
                ans.append(x - (bit >> 1))
        return ans
