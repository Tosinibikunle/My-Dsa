from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        index_map = defaultdict(list)

        for i, val in enumerate(nums):
            index_map[val].append(i)

        answer = []

        for q in queries:
            indices = index_map[nums[q]]

            if len(indices) == 1:
                answer.append(-1)
                continue

            # Binary search for position of q in the sorted indices list
            pos = bisect_left(indices, q)
            size = len(indices)
            min_dist = float('inf')

            # Check neighbor to the right (wrap around if needed)
            right_idx = indices[(pos + 1) % size]
            d1 = abs(q - right_idx)
            min_dist = min(min_dist, min(d1, n - d1))

            # Check neighbor to the left (wrap around if needed)
            left_idx = indices[(pos - 1) % size]
            d2 = abs(q - left_idx)
            min_dist = min(min_dist, min(d2, n - d2))

            answer.append(min_dist)

        return answer
