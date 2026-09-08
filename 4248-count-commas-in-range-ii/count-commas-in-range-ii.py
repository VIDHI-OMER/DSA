class Solution:
    def countCommas(self, n: int) -> int:
        st=1000
        res=0
        while(st<=n):
            res+=(n-st+1)
            st*=(10**3)
        return res