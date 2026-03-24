class Solution(object):
    def constructProductMatrix(self, grid):

        MOD = 12345
        m ,n = len(grid),len(grid[0])

        # 1. Flatten 
        arr =[]
        for row in grid:
            arr.extend(row)
        size = len(arr)

        # Prefix 
        prefix = [1] * size
        for i in range(1,size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD


        # Suffix 
        suffix = [1] * size
        for i in range(size-2,-1,-1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        # Result
        res = []
        for i in range(size):
            res.append((prefix[i] * suffix[i]) % MOD)

        # Convert into 2D Array
        ans = []
        idk = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(res[idk])
                idk += 1
            ans.append(row)
        
        return ans



        
