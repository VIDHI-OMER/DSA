from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        c=0
        dirr=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and vis[i][j]==0:
                    q=deque()
                    q.append((i,j))
                    vis[i][j]=1
                    ans=1
                    while(q):
                        x,y=q.popleft()
                        for dx,dy in dirr:
                            nx=x+dx 
                            ny=y+dy
                            if(nx>=0 and nx<n and ny>=0 and ny<m and grid[nx][ny]==1 and vis[nx][ny]==0):
                                vis[nx][ny]=1
                                ans+=1
                                q.append((nx,ny))
                    c=max(c,ans)
        return c