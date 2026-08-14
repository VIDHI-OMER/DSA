class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        i=j=0
        mp={}
        maxi=float('-inf')
        while(j<n):
            if s[j] in mp:
                mp[s[j]]+=1
            else:
                mp[s[j]]=1
            while(mp[s[j]]>2):
                mp[s[i]]-=1
                i+=1
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi