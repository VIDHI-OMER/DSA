class Solution:
    def climbStairs(self, n: int) -> int:
        def dun(n,memo):
            if memo[n]!=-1:
                return memo[n]
            if n<=1:
                memo[n]=1   
                return memo[n]
            memo[n]=dun(n-1,memo)+dun(n-2,memo)
            return memo[n]
        memo=[-1]*(n+1)
        return dun(n,memo)
        
