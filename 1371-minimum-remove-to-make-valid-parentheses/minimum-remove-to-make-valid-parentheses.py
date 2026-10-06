class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n=len(s)
        res=''
        c=0
        for i in s:
            if i.isalpha():
                res+=i
            elif i=='(':
                c+=1
                res+=i
            elif i==')':
                if c>0:
                    c-=1
                    res+=i
        ans=''
        for i in range(len(res)-1,-1,-1):
            if res[i]=='(' and c>0:
                c-=1
            else:
                ans+=res[i]
        return ans[::-1]
                    
                

            
                

                