class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        def dfs(i,j,vis):
            if i>=n or i<0 or j<0 or j>=m or grid[i][j]==0 or vis[i][j]:
                return 0
            vis[i][j]=1
            return grid[i][j]+dfs(i,j-1,vis)+dfs(i-1,j,vis)+dfs(i,j+1,vis)+dfs(i+1,j,vis)
        maxi=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0 and vis[i][j]==0:
                    maxi=max(maxi,dfs(i,j,vis))
        return maxi