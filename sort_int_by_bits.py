class Solution:
    def sortByBits(self, arr):
        # create 15 buckets
        lst = [[] for _ in range(15)]

        # fill buckets
        for num in arr:
            bits = bin(num).count('1')
            lst[bits].append(num)

        # build answer
        ans = []
        for bucket in lst:
            bucket.sort()
            for num in bucket:
                ans.append(num)

        return ans
