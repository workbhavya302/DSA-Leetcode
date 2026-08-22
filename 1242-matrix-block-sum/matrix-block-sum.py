class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                dp[r][c] = (mat[r - 1][c - 1] + dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1])

        ans = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(rows - 1, i + k), min(cols - 1, j + k)
                ans[i][j] = (dp[r2 + 1][c2 + 1] - dp[r1][c2 + 1] - dp[r2 + 1][c1] + dp[r1][c1])
                             
        return ans
