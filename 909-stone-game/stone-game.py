class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        tot=sum(piles)
        memo=[[-1]*n for _ in range(n)]
        def sol(i,j):
            if(i>j):
                return 0
            if(i==j):
                return piles[i]
            if(memo[i][j]!=-1):
                return memo[i][j]
            takei=piles[i]+min(sol(i+2,j),sol(i+1,j-1))
            takej=piles[j]+min(sol(i,j-2),sol(i+1,j-1))
            memo[i][j]=max(takei,takej)
            return memo[i][j]
        p1=sol(0,n-1)
        p2=tot-p1
        return p1>p2        