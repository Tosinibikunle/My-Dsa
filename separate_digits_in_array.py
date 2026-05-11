class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #best way to solve without using divide and reminder method
        ans=[] #create a list for final answer
        for i in nums:
            i=str(i) #convert the number into string
            for j in i: #loop into the string number
                ans.append(int(j)) #add it after converting it into int
        return ans #return the answer
