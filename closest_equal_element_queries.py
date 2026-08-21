from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: list[int], queries:
        n = len(nums)
        index_map = defaultdict(list)

        for i, val in enumerate(nums):
            index_map[val].append(i)

        answer = []

        for q in queries:
            indices = index_map[nums[q]]

            if len(indices) == 1:
                answer.append(-1)
                
            pos = bisect_left(indices, q)
            size = len(indices)
            min_dist = float('inf')

        
            right_idx = indices[(pos + 1) % size]
            d1 = abs(q - right_idx)
            min_dist = min(min_dist, min(d1, n - d1))

            left_idx = indices[(pos - 1) % size]
            d2 = abs(q - left_idx)
            min_dist = min(min_dist, min(d2, n - d2))

            answer.append(min_dist)

        return answer
