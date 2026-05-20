class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)

        freq = [0] * (n + 1)
        ans = [0] * n

        cnt = 0

        for i in range(n):

            freq[A[i]] += 1
            if freq[A[i]] == 2:
                cnt += 1

            freq[B[i]] += 1
            if freq[B[i]] == 2:
                cnt += 1

            ans[i] = cnt

        return ans
