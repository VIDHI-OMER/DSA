class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        d={}
        def solve(i,j):
            if i==n:
                return 0
            if j>=(i+1):
                return float('inf')
            if (i,j) in d:
                return d[(i,j)]
            below=triangle[i][j]+solve(i+1,j)
            dia=triangle[i][j]+solve(i+1,j+1)
            d[(i,j)]=min(below,dia)
            return d[(i,j)]
        return solve(0,0)