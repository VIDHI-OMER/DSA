class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n=len(board)
        m=len(board[0])
        vis=[[0]*m for _ in range(n)]
        c=0
        def dfs(i,j):
            if(i<0 or j<0 or i>=n or j>=m or board[i][j]!='X' or vis[i][j]==1):
                return 0
            vis[i][j]=1
            return dfs(i+1,j) or dfs(i-1,j) or dfs(i,j-1) or dfs(i,j+1)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='X' and vis[i][j]==0:
                    c+=1
                    dfs(i,j)
        return c

        