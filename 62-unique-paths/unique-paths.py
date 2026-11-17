class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={}
        def ct(i,j):
            
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in d:
                return d[(i,j)]
            
            d[(i,j)]=ct(i+1,j)+ct(i,j+1)
            return d[(i,j)]
        return ct(0,0)
        