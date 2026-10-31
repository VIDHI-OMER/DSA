class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        d={}
        def coin(amt,i):
            if i>=n:
                if amt==0:
                    return 0
                return float('inf')
            if (amt,i) in d:
                return d[(amt,i)]
            if amt-coins[i]<0:
                return coin(amt,i+1)
            else:
                take=1+coin(amt-coins[i],i)
                nottake=coin(amt,i+1)
                d[(amt,i)]=min(take,nottake)
                return d[(amt,i)]
        ans=coin(amount,0)
        if ans==float('inf'):
            return -1
        return ans