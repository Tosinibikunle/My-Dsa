class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        store = {}

        for val in s:
            if val in store:
                store[val] += 1
            else:
                
                store[val] = 1

        
        for i in range(len(s)):

            if store[s[i]] == 1:

                return i

        return - 1
        