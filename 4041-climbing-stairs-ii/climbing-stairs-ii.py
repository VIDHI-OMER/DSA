class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        d={}
        def solve(i):
            if i==n:
                return 0
            cst=float('inf')
            if i in d:
                return d[i]
            j=i+1
            if j<=n:
                cst=solve(j)+costs[j-1]+(j-i)**2
            j=i+2
            if j<=n:
                cst=min(cst,costs[j-1]+(j-i)**2+solve(j))
            j=i+3
            if j<=n:
                cst=min(cst,costs[j-1]+(j-i)**2+solve(j))
            d[i]=cst
            return d[i]
        return solve(0)
            
            