class Solution:
    def maxSumTrionic(self, nums):

        n = len(nums)
        res = -10**16

        i = 1
        while i < n - 2:

            a = b = i
            net = nums[a]

            while b + 1 < n and nums[b + 1] < nums[b]:
                net += nums[b + 1]
                b += 1

            if a == b:
                i += 1
                continue

            c = b

            left = right = 0
            lx = rx = -10**18

            while a - 1 >= 0 and nums[a - 1] < nums[a]:
                left += nums[a - 1]
                lx = max(lx, left)
                a -= 1

            if a == i:
                i += 1
                continue

            while b + 1 < n and nums[b + 1] > nums[b]:
                right += nums[b + 1]
                rx = max(rx, right)
                b += 1

            if b == c:
                i += 1
                continue

            res = max(res, lx + net + rx)
            i = b

        return res
