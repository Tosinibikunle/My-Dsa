class Solution:
    def maxArea(self, row):
        row.sort(reverse=True)
        ans = 0
        for i in range(len(row)):
            temp = row[i] * (i + 1)
            ans = max(ans, temp)
        return ans

    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        temp = [0] * n
        ans = 0

        for i in range(m-1, -1, -1):
            for j in range(n):
                if matrix[i][j] == 0:
                    temp[j] = 0
                else:
                    temp[j] += 1

            ans = max(ans, self.maxArea(temp))

        return ans
