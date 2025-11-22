class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []
        n = len(nums)
        param = n * 2

        for i in range(param):

            if i < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i - n])

        return ans
