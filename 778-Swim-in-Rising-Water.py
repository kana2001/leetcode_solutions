class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = grid[0][0]
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        # val, r, c

        visit = set()
        while minHeap:
            depth, r, c = heapq.heappop(minHeap)

            res = max(res, grid[r][c])
            if r == ROWS-1 and c == COLS-1:
                return res

            visit.add((r,c))
            dirs = [(1,0), (-1,0), (0, -1), (0, 1)]

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if (nr, nc) in visit or nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                heapq.heappush(minHeap, (grid[nr][nc], nr, nc))