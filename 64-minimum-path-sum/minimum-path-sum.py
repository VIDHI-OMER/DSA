class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        d={}
        def solve(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return float('inf')
            if i==m-1 and j==n-1:
                return grid[i][j]
            if (i,j) in d:
                return d[(i,j)]
            left=grid[i][j]+solve(i+1,j)
            right=grid[i][j]+solve(i,j+1)
            d[(i,j)]= min(left,right)
            return d[(i,j)]
        return solve(0,0)

        
