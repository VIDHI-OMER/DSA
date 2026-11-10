class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        d={}
        def call(i):
            if i==n:
                return 0
            if i in d:
                return d[i]
            res=float('inf')
            for j in range(i+1,min(i+3,n)+1):
                c=costs[j-1]+(j-i)**2
                res=min(res,c+call(j))
            d[i]=res
            return d[i]
        return call(0)