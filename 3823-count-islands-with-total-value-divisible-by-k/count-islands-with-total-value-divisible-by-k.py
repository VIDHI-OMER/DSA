class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j,vis):
            if i<0 or i>=n or j<0 or j>=m or vis[i][j] or grid[i][j]==0:
                return 0
            vis[i][j]=1
            return grid[i][j]+dfs(i-1,j,vis)+dfs(i,j-1,vis)+dfs(i+1,j,vis)+dfs(i,j+1,vis)
        c=0
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and vis[i][j]==0:
                    f=dfs(i,j,vis)
                    if f%k==0:
                        c+=1
        return c

        