class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        def dfs(i,j,vis):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            if vis[i][j]:
                return True
            if grid[i][j]==1:
                return True
            vis[i][j]=1
            a=dfs(i+1,j,vis)
            b=dfs(i,j+1,vis)
            c=dfs(i-1,j,vis)
            d=dfs(i,j-1,vis)
            return a and b and c and d
        c=0 
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and vis[i][j]==0:
                    if (dfs(i,j,vis)):
                        c+=1
        return c