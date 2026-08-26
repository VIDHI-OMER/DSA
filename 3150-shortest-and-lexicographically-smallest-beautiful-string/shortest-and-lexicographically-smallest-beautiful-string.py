class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        i=j=0
        mini=float('inf')
        ans=''
        c=0
        while(j<n):
            if s[j]=='1':
                c+=1
            while(c==k):
                curr=s[i:j+1]
                l=j-i+1
                if l<mini:
                    mini=l
                    ans=curr
                elif l==mini:
                    ans=min(ans,curr)
                if s[i]=='1':
                    c-=1
                i+=1
            while c>k:
                if(s[i]=='1'):
                    c-=1
                i+=1
            
            j+=1
        return ans
                        


            
        