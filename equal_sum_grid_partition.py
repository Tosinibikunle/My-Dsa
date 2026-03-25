class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rowSum = []
        colSum = []

        m = len(grid)
        n = len(grid[0])

        # Compute row sums
        for i in range(m):
            temp = 0
            for j in range(n):
                temp += grid[i][j]
            rowSum.append(temp)

        # Compute column sums
        for j in range(n):
            temp = 0
            for i in range(m):
                temp += grid[i][j]
            colSum.append(temp)

        # Total sum of grid
        totalSum = sum(sum(row) for row in grid)

        # Check row partition
        currRowSum = 0
        for i in range(m):
            currRowSum += rowSum[i]
            if currRowSum == totalSum - currRowSum:
                return True

        # Check column partition
        currColSum = 0
        for i in range(n):
            currColSum += colSum[i]
            if currColSum == totalSum - currColSum:
                return True

        return False
