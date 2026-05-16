class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        base = [*range(1, n + 1), n]
        
        return sorted(nums) == base
