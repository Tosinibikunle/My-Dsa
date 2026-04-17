class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        index_map = {}
        min_distance = float('inf')

        for j, num in enumerate(nums):
            # Look up num — earlier entries stored reverse(nums[i]) as key
            if num in index_map:
                min_distance = min(min_distance, j - index_map[num])

            # Store reverse(num) → j, overwriting older index (only need the latest)
            reversed_num = int(str(num)[::-1])
            index_map[reversed_num] = j

        return min_distance if min_distance != float('inf') else -1
