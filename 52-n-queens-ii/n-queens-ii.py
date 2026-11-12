class Solution:
    def totalNQueens(self, n: int) -> int:
        c=0
        board=[['.']*n for _ in range(n)]
        def safe(row, col):
            #upper left diagonal check
            nwcol=col
            nwrow=row
            while(row>=0 and col>=0):
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1
            col=nwcol
            row=nwrow
            #left side check
            while(col>=0):
                if board[row][col]=='Q':
                    return False
                col-=1
            # lower left diagonal check
            col=nwcol
            row=nwrow
            while(row<n and col>=0):
                if board[row][col]=='Q':
                    return False
                col-=1
                row+=1
            return True
        def solve(col):
            nonlocal c
            if col==n:
                c+=1
                return 
            for row in range(n):
                if safe(row,col):
                    board[row][col]='Q'
                    solve(col+1)
                    board[row][col]='.'
        solve(0)
        return c
        