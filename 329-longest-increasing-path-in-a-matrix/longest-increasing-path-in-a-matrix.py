class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            ans=1
            if i+1<n and matrix[i+1][j]>matrix[i][j]:
                ans=max(ans,1+dfs(i+1,j))
            if j+1<m and matrix[i][j+1]>matrix[i][j]:
                ans=max(ans,1+dfs(i,j+1))
            if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                ans=max(ans,1+dfs(i-1,j))
            if j-1>=0 and matrix[i][j-1]>matrix[i][j]:
                ans=max(ans,1+dfs(i,j-1))
            dp[(i,j)]=ans
            return ans
        mx=0
        for i in range(n):
            for j in range(m):
                mx=max(mx,dfs(i,j))
        return mx
