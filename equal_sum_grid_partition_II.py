class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(map , r1,r2,c1,c2 ,diff,grid) :
            rows = r2 - r1 + 1
            cols = c2 - c1 + 1
            if rows * cols == 1 :
                return False
            if rows == 1 :
                return diff == grid[r1][c1] or diff == grid[r1][c2]

            if cols == 1 :
                return diff == grid[r1][c1] or diff == grid[r2][c1]
            return  map.get(diff , 0) > 0

        m , n = len(grid) , len(grid[0])

        top = defaultdict(int)
        bottom = defaultdict(int)
        left = defaultdict(int)
        right = defaultdict(int)



        # initializing
        total = 0
        for row in grid :
            for val in row :
                total += val
                bottom[val] += 1
                right[val] += 1

        # checking horizental rows
        top_sum = 0
        for i in range(m-1) :
            for j in range(n) :
                top_sum += grid[i][j]
                top[grid[i][j]] += 1
                bottom[grid[i][j]] -= 1

            bottom_sum = total - top_sum
            if bottom_sum == top_sum :
                return True

            if top_sum > bottom_sum :
                diff = top_sum - bottom_sum 
                if check(top , 0 , i , 0 , n-1 , diff,grid) :
                    return True
            else :
                diff = bottom_sum - top_sum
                if check(bottom , i+1 , m-1 , 0 , n-1, diff, grid) :
                    return True



        left_sum = 0
        for j in range(n-1) :
            for i in range(m) :
                val = grid[i][j]
                left_sum += val
                left[val] += 1
                right[val] -= 1
            if left_sum == (total-left_sum) :
                return True

            if left_sum > (total-left_sum) :
                diff = left_sum - (total-left_sum)
                if check(left , 0,m-1,0,j,diff,grid) :
                    return True
            else :
                diff = (total-left_sum) - left_sum
                if check(right , 0,m-1,j+1,n-1,diff,grid):
                    return True

        return False

        






        
