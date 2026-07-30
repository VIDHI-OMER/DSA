class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        res=0
        val=1
        while(n>0):
            t=min(8,n)
            res+=t*val
            n-=t
            val+=1
        return res