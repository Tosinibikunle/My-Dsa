class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        seen = set()
        duplicate = -1

        # Find the duplicate using a set
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        # The missing number is the one from 1..n not in the set
        for i in range(1, n + 1):
            if i not in seen:
                return [duplicate, i]
