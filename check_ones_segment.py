class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        idx = 0
        n = len(s)
        flag = True

        while idx < n:
            if not flag and s[idx] == '1':
                return False

            if s[idx] == '0':
                flag = False

            idx += 1

        return True
