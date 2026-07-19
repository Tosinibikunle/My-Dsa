from collections import defaultdict

class Solution:
    MOD = 10**9 + 7

    def specialTriplets(self, nums):
        mppPrev = defaultdict(int) 
        mppNext = defaultdict(int)

    
        for x in nums:
            mppNext[x] += 1

        ans = 0
        n = len(nums)

        for i in range(n):
            cur = nums[i]


            mppNext[cur] -= 1
            if mppNext[cur] == 0:
                del mppNext[cur]

            if i - 1 >= 0:
                mppPrev[nums[i - 1]] += 1

            req = cur * 2 

            if req in mppPrev and req in mppNext:
                cnt1 = mppPrev[req]
                cnt2 = mppNext[req]
                ans = (ans + (cnt1 * cnt2) % self.MOD) % self.MOD

        return ans
