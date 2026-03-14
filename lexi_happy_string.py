
class Solution:
    def __init__(self):
        self.count = 0

    def getHappyString(self, n: int, k: int) -> str:

        size = 3 * (2 ** (n - 1))

        if k > size:
            return ""

        return self.helper(n, k, "")

    def helper(self, n, k, s):

        if len(s) == n:
            self.count += 1

            if self.count == k:
                return s

            return ""

        if len(s) == 0 or s[-1] != 'a':
            res = self.helper(n, k, s + 'a')
            if res != "":
                return res

        if len(s) == 0 or s[-1] != 'b':
            res = self.helper(n, k, s + 'b')
            if res != "":
                return res

        if len(s) == 0 or s[-1] != 'c':
            res = self.helper(n, k, s + 'c')
            if res != "":
                return res

        return ""
