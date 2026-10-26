class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        def dfs(i,j,vis):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]=='0' or vis[i][j]:
                return 
            vis[i][j]=1
            dfs(i+1,j,vis)
            dfs(i,j+1,vis)
            dfs(i,j-1,vis)
            dfs(i-1,j,vis)
            return
        c=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and vis[i][j]==0:
                    c+=1
                    dfs(i,j,vis)
        return c