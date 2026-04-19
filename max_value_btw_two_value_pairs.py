class Solution(object):
    def maxDistance(self, nums1, nums2):
        max_dist = 0
        i = 0  # Pointer for nums1
        j = 0  # Pointer for nums2
        n1, n2 = len(nums1), len(nums2)
        
        # Traverse both arrays using a two-pointer technique
        while i < n1 and j < n2:
            # Check the validity condition: i <= j is implicitly handled
            # because we advance j when the value condition is met.
            if nums1[i] <= nums2[j]:
                # Update max_dist if the current gap is larger
                if j - i > max_dist:
                    max_dist = j - i
                # Try to increase the distance by moving the right pointer
                j += 1
            else:
                # If nums1[i] is too big, move the left pointer forward
                i += 1
                # Ensure j doesn't lag behind i to keep the distance non-negative
                if i > j:
                    j = i
                        
        return max_dist
