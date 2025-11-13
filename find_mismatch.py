class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        p1 = 0
        p2 = 1
        res = []

        

        for i in range(len(nums)):

            if nums[p1] < nums[p2]:

                p1 += 1
                p2 += 1

            elif nums[p1] > nums[p2]:
                res.append(nums[p2])
                res.append(nums[p1] + 1)

                return res


            else:
                res.append(nums[p1])
                res.append(nums[p1] + 1)

                return res

        


        