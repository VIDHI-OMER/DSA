class Solution:
    def partitionString(self, s: str) -> int:
        n=len(s)
        d=[-1]*26
        c=0
        st=0
        for i in range(n):
            ch=s[i]
            if d[ord(s[i])-ord('a')]>=st:
                c+=1
                st=i
            d[ord(s[i])-ord('a')]=i
        return c+1
        

