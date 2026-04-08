class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD=10**9 + 7
        for q in queries:
            idx=q[0]
            while idx<=q[1]:
                nums[idx]=(nums[idx]*q[3]) % MOD
                idx+=q[2]
        b=0
        for i in nums:
            b^=i
        return b

        
