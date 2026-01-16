class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def maxLen(Bars):
            count,length = 2,2
            for i in range(1,len(Bars)):
                if Bars[i] - Bars[i-1] == 1: count += 1
                else: count = 2
                length = max(length, count)
            return length
        hBars.sort(), vBars.sort()
        side = min(maxLen(hBars), maxLen(vBars))
        return side * side
