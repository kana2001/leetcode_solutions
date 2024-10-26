class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            dirs = [[1,0], [-1,0], [0,1],[0,-1]]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS) and matrix[nr][nc] > matrix[r][c]:
                    search = 1 + dfs(nr,nc)
                    res = max(search, res)
            dp[(r,c)] = res
            return res
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))
        return res