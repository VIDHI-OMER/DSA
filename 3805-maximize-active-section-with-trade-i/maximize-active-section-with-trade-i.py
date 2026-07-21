class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        numZero=[]
        i=0
        one=s.count('1')
        while(i<n):
            if s[i]=='0':
                st=i
                while i<n and s[i]=='0':
                    i+=1
                numZero.append(i-st)
            else:
                i+=1
        
        ans=0
        for i in range(1,len(numZero)):
            d=numZero[i]+numZero[i-1]
            ans=max(ans,d)
        return ans+one
            
    