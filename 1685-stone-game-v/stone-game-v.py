class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n=len(stoneValue)
        preSum=[]
        c=0
        memo = [[-1]*n for _ in range(n)]
        for i in stoneValue:
            c+=i
            preSum.append(c)
        #print(preSum)
        def solve(l,r):
            ct=0
            if(l>=r):
                return 0
            if memo[l][r]!=-1:
                return memo[l][r]
            for i in range(l,r):
                if(l>0):
                    lft=preSum[i]-preSum[l-1]
                else:
                    lft=preSum[i]
                rgt=preSum[r]-preSum[i]
                if lft<rgt:
                    ct=max(ct,lft+solve(l,i))
                elif lft>rgt:
                    ct=max(ct,rgt+solve(i+1,r))
                else:
                    ct=max(ct,lft+solve(l,i),rgt+solve(i+1,r))
            memo[l][r]=ct
            return ct

        return solve(0,n-1)