class Solution:
    def minRemoval(self, nums, k):
        n = len(nums)
        nums.sort()
        
        # Find the longest contiguous subarray where max <= k * min
        max_length = 1  # At minimum, a single element is always balanced
        
        left = 0
        for right in range(n):
            # For current window [left, right], min is nums[left], max is nums[right]
            while left < right and nums[right] > k * nums[left]:
                left += 1
            
            # Now the window [left, right] is balanced
            max_length = max(max_length, right - left + 1)
        
        return n - max_length
