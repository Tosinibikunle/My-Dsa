class Solution(object):
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        # memo[i][j][cost] stores the max score from (i, j) given current 'cost'
        memo = [[[-1 for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]

        def solve(i, j, cost):
            # 1. Out of bounds check
            if i >= m or j >= n:
                return float("-inf")

            # 2. Update cost if current cell is positive
            current_cost = cost + (1 if grid[i][j] > 0 else 0)
            
            # 3. Check budget constraint
            if current_cost > k:
                return float("-inf")

            # 4. Return to destination base case
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            # 5. Check Memoization
            if memo[i][j][current_cost] != -1:
                return memo[i][j][current_cost]

            # 6. Recursive exploration (Right and Down)
            res_right = solve(i, j + 1, current_cost)
            res_down = solve(i + 1, j, current_cost)

            best_path = max(res_right, res_down)

            # 7. Calculate result
            if best_path == float("-inf"):
                ans = float("-inf")
            else:
                ans = grid[i][j] + best_path

            memo[i][j][current_cost] = ans
            return ans

        final_ans = solve(0, 0, 0)
        return final_ans if final_ans != float("-inf") else -1
