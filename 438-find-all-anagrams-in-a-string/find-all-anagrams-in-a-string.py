class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n=len(s)
        m=len(p)
        l=[]
        freq1={}
        mp={}
        k=j=0
        for i in p:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        #print(freq1)
        while(j<n):
            if s[j] in mp:
                mp[s[j]]+=1
            else:
                mp[s[j]]=1
            if (j-k+1>m):
                mp[s[k]]-=1
                if mp[s[k]]==0:
                    del mp[s[k]]
                k+=1
            if mp==freq1:
                l.append(k)
            j+=1
        
        return l
            



