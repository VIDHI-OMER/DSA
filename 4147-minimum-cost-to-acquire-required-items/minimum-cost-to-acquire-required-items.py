class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
       
        common=min(need1, need2)
        
        cst1=cost1*need1+cost2*need2
        cst2=costBoth*max(need1,need2)
        cst3=common*costBoth+(need1-common)*cost1+(need2-common)*cost2

        return min(cst1,cst2,cst3)
        
        