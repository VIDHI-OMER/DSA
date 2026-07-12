class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        left=[0]*n
        right=[0]*n
        pref=[0]*n
        lf=-1
        ans=[]
        for i in range(len(s)):
            if (s[i]=='|'):
                lf=i
                left[i]=lf
            else:
                left[i]=lf
        print(left)
        rg=-1
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='|'):
                rg=i
                right[i]=rg
            else:
                right[i]=rg
        print(right)
        now=0
        for i in range(len(s)):
            if s[i]=='*':
                now+=1
                pref[i]=now
            else:
                pref[i]=now
        print(pref)
        for l,r in queries:
            st=right[l]
            ed=left[r]
            if st==-1 or ed==-1 or st>=ed:
                ans.append(0)
            else:
                ans.append(pref[ed]-pref[st])
        print(ans)
        return ans

