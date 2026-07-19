class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n=len(s)
        res=[]
        freq=[0]*26
        idx=[-1]*26
        for i in range(n):
            ch=s[i]
            idx[ord(ch)-ord('a')]=i
        for i in range(n):
            ch=s[i]
            indd=ord(ch)-ord('a')
            if(freq[indd]==True):
                continue 
            while (len(res)>0 and res[-1]>ch and idx[ord(res[-1])-ord('a')]>i):
                freq[ord(res[-1])-ord('a')]=0
                res.pop()
            res.append(ch)
            freq[indd]=True
        return ''.join(res)
                
        