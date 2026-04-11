class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Dictionary to store number: [list of indices]
        mpp = {}
        n = len(nums)
        
        if n <= 2:
            return -1
            
        ans = float('inf')

        # Step 1: Group indices by number
        for i, val in enumerate(nums):
            if val not in mpp:
                mpp[val] = []
            mpp[val].append(i)

        # Step 2: Calculate distances for numbers appearing >= 3 times
        for indices in mpp.values():
            if len(indices) < 3:
                continue
            
            # Check every window of 3 indices
            for i in range(len(indices) - 2):
                current_dist = 2 * (indices[i + 2] - indices[i])
                if current_dist < ans:
                    ans = current_dist

        return -1 if ans == float('inf') else ans
