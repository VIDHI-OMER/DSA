class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        def solve(i,j,ct):
            
            if grid[i][j]=='(':
                ct+=1
            else:
                ct-=1
            if ct<0:
                return False
            if memo[i][j][ct]!=-1:
                return memo[i][j][ct]
            if (i==n-1 and j==m-1):
                return ct==0
            res=False
            if i+1<n:
                res=solve(i+1,j,ct)
            if not res and j+1<m:
                res=solve(i,j+1,ct)
            memo[i][j][ct]=res
            return res
        memo=[[[-1]*(n+m) for _ in range(m)] for _ in range(n)]
        if grid[0][0]==')':
            return False
        if ((n+m-1)%2==1):
            return False
        return solve(0,0,0)
        