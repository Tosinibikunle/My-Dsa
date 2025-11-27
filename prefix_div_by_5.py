class Solution:
    def prefixesDivBy5(self, nums):
        val = 0
        ans = []

        for bit in nums:
            val = (val * 2 + bit) % 5  
            ans.append(val == 0)

        return ans
