class Solution:
    def uniquePathsWithObstacles(self, ob: list[list[int]]) -> int:
        n=len(ob)
        m=len(ob[0])
        d={}
        def count(i,j):
            if i<0 or i>=n or j<0 or j>=m or ob[i][j]==1:
                return 0
            if i==n-1 and j==m-1:
                return 1
            if (i,j) in d:
                return d[(i,j)]
            d[(i,j)]=count(i+1,j)+count(i,j+1)
            return d[(i,j)]
        return count(0,0)
            
