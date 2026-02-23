class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # binary code of lenght k
        # is it in s ?
        if len(s) < k:
            return False
        
        allCodeCount = 1 << k
        seenCode = set()
        # sliding window
        left = 0
        n = len(s)
        for right in range(n):
            num = s[right]
            if right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                currString = s[left:right + 1]
                seenCode.add(currString)
        return len(seenCode) == allCodeCount
