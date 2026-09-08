class Solution:
    def countCommas(self, n: int) -> int:
        low=1000
        comma=1
        res=0
        while low<=n:
            up=low*1000-1
            if up>n:
                up=n
            cout=up-low+1
            res+=(cout*comma)
            low=low*1000
            comma+=1
        return res



        
