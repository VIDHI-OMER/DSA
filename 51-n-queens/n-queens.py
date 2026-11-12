class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        ans=[]
        l=[['.']*n for _ in range(n)]
        def Safe(row,col):
            nwrow=row
            nwcol=col
            while(row>=0 and col>=0):
                if l[row][col]=='Q':
                    return False
                row-=1
                col-=1
            col=nwcol
            row=nwrow
            while(col>=0):
                if l[row][col]=='Q':
                    return False
                col-=1
            col=nwcol
            row=nwrow
            while(row<n and col>=0):
                if l[row][col]=='Q':
                    return False
                col-=1
                row+=1
            return True

        def solve(col):
            if col==n:
                ans.append([''.join(row) for row in l])
                return
            for row in range(0,n):
                if Safe(row,col):
                    l[row][col]='Q'
                    solve(col+1)
                    l[row][col]='.'
        
        solve(0)
        return ans
        