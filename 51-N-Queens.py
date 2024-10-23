class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = set()
        cols = set()
        pos_diag = set()
        neg_diag = set()

        board = ['.' * n for i in range(n)]

        res = []

        def dfs(r):
            # if r < 0 or r >= n or c < 0 or c >= n or (r,c) in queens:
            #     return

            if r == n:
                ans = board.copy()
                res.append(ans)
                return

            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue

                board[r] = board[r][:c] + 'Q' + board[r][c+1:]
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                dfs(r+1)

                board[r] = '.' * n
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)

        dfs(0)
        return res
        

            

                
            
