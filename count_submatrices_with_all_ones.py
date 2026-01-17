class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    # Step 1: Horizontal accumulation
                    if j > 0:
                        mat[i][j] += mat[i][j - 1]

                    # Step 2: Count submatrices ending at (i, j)
                    min_width = mat[i][j]
                    k = i
                    while k >= 0 and mat[k][j] > 0:
                        min_width = min(min_width, mat[k][j])
                        count += min_width
                        k -= 1
        return count
