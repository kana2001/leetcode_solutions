class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1,0), (-1,0), (0, -1), (0, 1)]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 0:
                return
            
            grid[r][c] = 1
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
        
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS-1, i)

        for j in range(ROWS):
            dfs(j, 0)
            dfs(j, COLS-1)

        res = 0
        for i in range(1, ROWS - 1):
            for j in range(1, COLS -1):
                if grid[i][j] == 0:
                    res +=1
                    dfs(i,j)
        return res