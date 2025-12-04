class Solution(object):
    def countTrapezoids(self, points):
        """
        Count valid trapezoids formed by points where trapezoids have
        horizontal parallel bases (same y-coordinates)

        :type points: List[List[int]]
        :rtype: int
        """
        M = 10**9 + 7
        y_count = {}

        for x, y in points:
            if y in y_count:
                y_count[y] += 1
            else:
                y_count[y] = 1

        counts = list(y_count.values())
        r = 0
        s = 0

        for c in counts:
            if c >= 2:

                w = c * (c - 1) // 2

                r += w * s

                s += w

        return r % M
