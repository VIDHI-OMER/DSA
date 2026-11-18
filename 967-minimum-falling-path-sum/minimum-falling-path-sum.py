class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        d={}
        def solve(i,j):
            if j<0 or j>=n:
                return float('inf')
            if i==n:
                return 0
            if (i,j) in d:
                return d[(i,j)]
            
            below=matrix[i][j]+solve(i+1,j)
            dilft=matrix[i][j]+solve(i+1,j-1)
            dirgt=matrix[i][j]+solve(i+1,j+1)

            d[(i,j)]= min(below,dilft,dirgt)
            return d[(i,j)]
        ans = float('inf')
        for j in range(n):
            ans=min(ans,solve(0,j))
        return ans

