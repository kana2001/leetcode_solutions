class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l,r = 0, COLS * ROWS - 1
        # 11 -> [2][3]
        # i = 4, [2][0]
        # i = 11, r = 11 // ROWS = 2, c = 11 % ROWS

        while l <= r:
            m = (l+r) // 2
            row,col = m // COLS, m % COLS
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False
            if target < matrix[row][col]:
                r = m - 1
            elif target > matrix[row][col]:
                l = m + 1
            else:
                return True
        return False
        