class Solution( object ):
    def firstMissingPositive( self, nums ):
        """
        :type nums: List[int]
        :rtype: int
        """
        limit = len(nums)
        for index in range(limit) :
            value = nums[index]
            while 1 <= value < limit and value != nums[value - 1] :
                nums[index], nums[value - 1] = nums[value - 1], value
                value = nums[index]
        for index in range(limit) :
            if nums[index] != index + 1 :
                return index + 1
        return limit + 1
