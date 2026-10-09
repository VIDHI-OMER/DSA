class Solution:
    def minInsertions(self, s: str) -> int:
        st=[]
        c=0
        i=0
        res=0
        while(i<len(s)):
            if s[i]=='(':
                c+=1
                i+=1
            else:
                if c>0:
                    c-=1
                else:
                    res+=1
                if i+1<len(s) and s[i+1]==')':
                    i+=2
                else:
                    res+=1
                    i+=1
        return res+(c*2)

            

        