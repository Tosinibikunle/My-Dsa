import bisect
from functools import cache

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        n = len(robots)
        if n == 0: return 0

        walls.sort()
        vp = sorted(zip(robots, distance))
        
        intervals = [[0] * 4 for _ in range(n)]
        for i in range(n):
            pos, d = vp[i]
            left_block = vp[i-1][0] if i > 0 else float('-inf')
            right_block = vp[i+1][0] if i < n - 1 else float('inf')

            intervals[i][0] = max(pos - d, left_block)
            intervals[i][1] = pos
            intervals[i][2] = pos
            intervals[i][3] = min(pos + d, right_block)

        def getCount(l, r):
            if l > r: return 0
            it1 = bisect.bisect_left(walls, l)
            it2 = bisect.bisect_right(walls, r)
            return it2 - it1

        # State: i = current robot index, prev_dir = direction of the previous robot
        # prev_dir: 0 = Left, 1 = Right, 2 = No previous robot (Start state)
        @cache
        def solve(i, prev_dir):
            # Base case: We've processed all robots
            if i == n:
                return 0
            
            # Determine where the previous robot ended based on its direction
            prev_r = float('-inf')
            if prev_dir == 0:
                prev_r = intervals[i-1][1]
            elif prev_dir == 1:
                prev_r = intervals[i-1][3]

            # Option 1: Current robot moves LEFT
            l1, r1 = intervals[i][0], intervals[i][1]
            walls_left = getCount(max(l1, prev_r + 1), r1)
            ans_left = walls_left + solve(i + 1, 0)

            # Option 2: Current robot moves RIGHT
            l2, r2 = intervals[i][2], intervals[i][3]
            walls_right = getCount(max(l2, prev_r + 1), r2)
            ans_right = walls_right + solve(i + 1, 1)

            # Return the best choice
            return max(ans_left, ans_right)

        # Start at robot 0, with '2' indicating no previous robot direction
        return solve(0, 2)
