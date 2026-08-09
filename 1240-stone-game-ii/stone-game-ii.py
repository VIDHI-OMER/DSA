class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        memo={}
        def dol(turn,i,M):
            if(i>=n):
                return 0
            if(turn,i,M) in memo:
                return memo[(turn,i,M)]
            stone=0
            if(turn==1):
                res=-1
            else:
                res=float('inf')
            for x in range(1,min(2*M,n-i)+1):
                stone+=piles[i+x-1]  #for getting the right idx value
                if(turn==1):         #Alice
                    res=max(res,stone+dol(0,i+x,max(M,x)))
                else:
                    res=min(res,dol(1,i+x,max(M,x)))
            memo[(turn,i,M)]=res
            return res
        
        return dol(1,0,1)


