class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        i=j=0
        maxi=0
        mp={}
        while(j<n):
            if s[j] not in mp:
                mp[s[j]]=1
            else:
                mp[s[j]]+=1
            while mp[s[j]]>1:
                mp[s[i]]-=1
                if mp[s[i]]==0:
                    del mp[s[i]]
                i+=1
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi



        