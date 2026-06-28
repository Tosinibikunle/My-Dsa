class Solution(object):
    def maximumElementAfterDecrementingAndRearr(self, arr):
        arr.sort()
        prev = 1
        arr[0] = 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], prev+1)
            prev = arr[i]
        
        return prev
