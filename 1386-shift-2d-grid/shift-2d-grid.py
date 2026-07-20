class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        
        for o in range(k):
            g=[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if j+1<n:
                        g[i][j + 1]=grid[i][j]
                    elif i+1<m:
                        g[i + 1][0]=grid[i][n - 1]
                    else:
                        g[0][0]=grid[m - 1][n - 1]
            grid=g
        return grid
                        
                        