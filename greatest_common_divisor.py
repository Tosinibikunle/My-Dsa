class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]

        for num in nums:
            maxi = max(maxi, num)
            mini = min(mini, num)

        return gcd(mini, maxi)
